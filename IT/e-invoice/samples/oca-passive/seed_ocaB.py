# PIANO B — semina fornitori OCA + storico posted per far accendere il tie-break.
# Per ogni venditore (CedentePrestatore) dei file normalizzati:
#   - crea il partner (match P.IVA in import -> "partner trovato")
#   - crea storico posted in cui QUEL fornitore, su quelle descrizioni, usa 22% S
#     (servizi), cioe' un'imposta SPECIFICA diversa dal default 22% M.
# Cosi' la predizione della patch impara "partner + descrizione -> 22% S".
# Uso: venv/bin/python odoo/odoo-bin shell -c odoo/odoo.conf -d <DB> < test-xml-oca/seed_ocaB.py
import re
import time
from pathlib import Path

BASE = Path('/home/odoo/activity/odoo/test-xml-oca')
NORM = BASE / 'normalized'
t0 = time.time()
company = env.company
env['res.lang']._activate_lang('it_IT')
env = env(context=dict(env.context, lang='it_IT'))
AccountTax = env['account.tax']

# --- estrai venditori + descrizioni 22% dai file normalizzati ---
sellers = {}
for p in sorted(NORM.glob('*.xml')) + sorted(NORM.glob('*.XML')):
    raw = p.read_text(encoding='utf-8', errors='ignore')
    m = re.search(r'<CedentePrestatore>(.*?)</CedentePrestatore>', raw, re.S)
    if not m:
        continue
    blk = m.group(1)
    paese = re.search(r'<IdFiscaleIVA>.*?<IdPaese>([^<]+)', blk, re.S)
    idcod = re.search(r'<IdFiscaleIVA>.*?<IdCodice>([^<]+)', blk, re.S)
    cf = re.search(r'<CodiceFiscale>([^<]+)', blk)
    den = re.search(r'<Denominazione>([^<]+)', blk)
    nome = re.search(r'<Nome>([^<]+)', blk)
    cog = re.search(r'<Cognome>([^<]+)', blk)
    key = (idcod.group(1) if idcod else (cf.group(1) if cf else None))
    if not key:
        continue
    name = den.group(1).strip() if den else (
        (cog.group(1).strip() + ' ' + nome.group(1).strip()) if (cog and nome) else key)
    s = sellers.setdefault(key, {
        'name': name, 'paese': paese.group(1) if paese else 'IT',
        'cf': cf.group(1) if cf else None, 'descs': set()})
    for det in re.findall(r'<DettaglioLinee>(.*?)</DettaglioLinee>', raw, re.S):
        al = re.search(r'<AliquotaIVA>([\d.]+)', det)
        de = re.search(r'<Descrizione>([^<]+)', det)
        if al and de and abs(float(al.group(1)) - 22.0) < 0.01:
            s['descs'].add(" ".join(de.group(1).split())[:120])

# --- risolvi 22% S (servizi) per firma e attivala ---
base_dom = [*AccountTax._check_company_domain(company),
            ('type_tax_use', '=', 'purchase'), ('amount_type', '=', 'percent')]
plain = [('l10n_it_withholding_type', '=', False), ('l10n_it_pension_fund_type', '=', False)]
tax_s = AccountTax.with_context(active_test=False).search(
    base_dom + plain + [('amount', '=', 22.0), ('tax_scope', '=', 'service'),
                        ('l10n_it_exempt_reason', '=', False)]).filtered(
    lambda t: all(r.factor_percent >= 0 for r in t.invoice_repartition_line_ids))
assert tax_s, "22% S non trovata"
tax_s = tax_s[0]
tax_s.active = True
expense = env['account.account'].search(
    [*env['account.account']._check_company_domain(company), ('account_type', '=', 'expense')], limit=1)
print(f"[{time.time()-t0:4.1f}s] imposta specifica scelta: {tax_s.name} (id {tax_s.id}) | conto {expense.code}")

# --- crea partner + storico ---
Partner = env['res.partner'].with_context(no_vat_validation=True)
n_part = n_bills = 0
for key, s in sellers.items():
    paese = s['paese']
    vat = ('IT' + key) if paese == 'IT' and key.isdigit() else (paese + key)
    partner = env['res.partner'].search(['|', ('vat', '=', vat), ('vat', '=', key)], limit=1)
    if not partner:
        vals = {'name': s['name'], 'is_company': True, 'vat': vat,
                'country_id': env['res.country'].search([('code', '=', paese)], limit=1).id}
        if paese == 'IT' and (s['cf'] or key).isdigit():
            vals['l10n_it_codice_fiscale'] = s['cf'] or key
        partner = Partner.create(vals)
        n_part += 1
    descs = sorted(s['descs']) or [f"Prestazione {s['name']}"]
    # per ogni descrizione, 4 fatture posted a 22% S (segnale forte per la predizione)
    for desc in descs[:6]:
        for i in range(4):
            move = env['account.move'].create({
                'move_type': 'in_invoice',
                'partner_id': partner.id,
                'invoice_date': f'2026-0{1 + (i % 5)}-15',
                'ref': f'HISTB/{key}/{abs(hash(desc)) % 9999}/{i}',
                'invoice_line_ids': [(0, 0, {
                    'name': desc, 'quantity': 1, 'price_unit': 100.0,
                    'account_id': expense.id, 'tax_ids': [(6, 0, [tax_s.id])]})],
            })
            move.action_post()
            n_bills += 1

env.cr.commit()
posted = env['account.move'].search_count([('move_type', '=', 'in_invoice'), ('state', '=', 'posted')])
print(f"[{time.time()-t0:4.1f}s] PIANO B seminato: {n_part} partner nuovi, {n_bills} fatture storiche 22% S")
print(f"           venditori: {len(sellers)} | posted totali nel DB: {posted}")

# Import osservativo del corpus OCA (l10n_it_fatturapa_in/tests/data) via lo
# stesso entry point dei test ufficiali. NESSUN ground truth: registra solo
# cosa succede (successo/errore, tipo, partner, righe, imposte, avvisi chatter).
# Uso: venv/bin/python odoo/odoo-bin shell -c odoo/odoo.conf -d <DB> < test-xml-oca/run_oca_import.py
import html as html_lib
import json
import re
import time
from pathlib import Path

BASE = Path('/home/odoo/activity/odoo/test-xml-oca')
# xml normalizzati (destinatario = azienda seed) + p7m originali per robustezza
files = sorted((BASE / 'normalized').glob('*.xml')) \
    + sorted((BASE / 'normalized').glob('*.XML')) \
    + sorted(BASE.glob('*.p7m'))

label = 'patched' if hasattr(env['account.move'], '_l10n_it_edi_search_taxes_for_import') else 'baseline'
env = env(context=dict(env.context, lang='it_IT'))
journal = env['account.journal'].search(
    [('type', '=', 'purchase'), ('company_id', '=', env.company.id)], limit=1)
default_account = journal.default_account_id
print(f"run OCA: {label} | {len(files)} file | journal {journal.name} | conto default {default_account.code}")


def messages_text(move):
    out = []
    for msg in move.message_ids:
        body = msg.body or ''
        out.append(html_lib.unescape(re.sub(r'<[^>]+>', ' ', body)).strip())
    return [m for m in out if m]


def td_of(raw):
    m = re.search(rb'<TipoDocumento>\s*([^<\s]+)', raw)
    return m.group(1).decode() if m else '?'


results = []
t_start = time.time()
for n, path in enumerate(files, start=1):
    raw = path.read_bytes()
    td = td_of(raw) if path.suffix.lower() == '.xml' else 'p7m'
    t0 = time.time()
    error = None
    moves = env['account.move']
    try:
        att = env['ir.attachment'].create({'name': path.name, 'raw': raw})
        moves = journal.with_context(default_move_type='in_invoice')._create_document_from_attachment(att.ids)
    except Exception as e:  # noqa: BLE001
        error = repr(e)[:250]
        env.cr.rollback()
    elapsed = round(time.time() - t0, 3)

    row = {'file': path.name, 'td': td, 'seconds': elapsed, 'error': error,
           'move_type': None, 'partner': None, 'partner_found': False,
           'n_lines': 0, 'taxes': [], 'accounts': [], 'chatter': []}
    if not error and moves:
        move = moves[0]
        lines = move.invoice_line_ids.filtered(lambda l: l.display_type == 'product')
        row.update({
            'move_type': move.move_type,
            'partner': move.partner_id.name or None,
            'partner_found': bool(move.partner_id),
            'n_lines': len(lines),
            'taxes': sorted({t.name for l in lines for t in l.tax_ids}),
            'accounts': sorted({l.account_id.code for l in lines if l.account_id}),
            'chatter': messages_text(move),
        })
    elif not error and not moves:
        row['error'] = 'nessun movimento creato'
    results.append(row)
    flag = 'ERR' if row['error'] else ('  ?' if not row['partner_found'] else '  .')
    print(f"[{n:2d}/{len(files)}] {flag} {td:5} {path.name:42.42} "
          f"{(row['move_type'] or '-'):11} righe={row['n_lines']} "
          f"chatter={len(row['chatter'])}")

total = round(time.time() - t_start, 1)
env.cr.rollback()  # non persistere: e' un test osservativo, DB resta pulito

# ---- sommario ----
n_err = sum(1 for r in results if r['error'])
n_nopart = sum(1 for r in results if not r['error'] and not r['partner_found'])
n_chatter = sum(1 for r in results if r['chatter'])
print()
print(f"===== SOMMARIO OCA ({label}) — {total}s / {len(results)} file =====")
print(f"errori/decode falliti : {n_err}")
print(f"import ok             : {len(results) - n_err}")
print(f"  di cui partner NON trovato: {n_nopart}")
print(f"  di cui con avvisi chatter : {n_chatter}")
print("\n-- errori --")
for r in results:
    if r['error']:
        print(f"  {r['td']:5} {r['file']:42.42} {r['error']}")

out = BASE / f"oca_results_{label}.json"
out.write_text(json.dumps({'label': label, 'total_seconds': total, 'files': results},
                          indent=1, ensure_ascii=False))
print(f"\ndettaglio in {out}")

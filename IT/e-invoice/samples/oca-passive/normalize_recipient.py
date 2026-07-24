#!/usr/bin/env python3
# Riscrive il CessionarioCommittente degli XML OCA con la P.IVA/CF dell'azienda
# seed (01984370377), cosi' l'import di l10n_it_edi li riconosce come fatture
# passive a noi intestate e popola le righe. Copie in normalized/, originali intatti.
# I p7m sono firmati: non riscrivibili, restano fuori.
import re
from pathlib import Path

BASE = Path('/home/odoo/activity/odoo/test-xml-oca')
OUT = BASE / 'normalized'
OUT.mkdir(exist_ok=True)
VAT = '01984370377'  # == l10n_it_codice_fiscale azienda seed; vat = IT + questo

def fix_block(block):
    # IdFiscaleIVA: forza IT + nostra P.IVA
    block = re.sub(r'(<IdFiscaleIVA>.*?<IdPaese>)[^<]*(</IdPaese>)',
                   rf'\g<1>IT\g<2>', block, flags=re.S)
    block = re.sub(r'(<IdFiscaleIVA>.*?<IdCodice>)[^<]*(</IdCodice>)',
                   rf'\g<1>{VAT}\g<2>', block, flags=re.S)
    # CodiceFiscale del cessionario
    block = re.sub(r'(<CodiceFiscale>)[^<]*(</CodiceFiscale>)',
                   rf'\g<1>{VAT}\g<2>', block)
    return block

n = 0
for p in sorted(BASE.glob('*.xml')) + sorted(BASE.glob('*.XML')):
    raw = p.read_text(encoding='utf-8', errors='ignore')
    new, cnt = re.subn(r'<CessionarioCommittente>.*?</CessionarioCommittente>',
                       lambda m: fix_block(m.group(0)), raw, flags=re.S)
    (OUT / p.name).write_text(new, encoding='utf-8')
    n += 1
    print(f"{'OK ' if cnt else 'NO-CC':5} {p.name}")
print(f"\n{n} file normalizzati in {OUT}")

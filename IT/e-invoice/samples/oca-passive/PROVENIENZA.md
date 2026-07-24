# FatturaPA di test — solo uso personale locale

Origine: OCA/l10n-italy, branch 16.0, `l10n_it_fatturapa_in/tests/data`
https://github.com/OCA/l10n-italy/tree/16.0/l10n_it_fatturapa_in/tests/data

Modulo di origine con licenza **AGPL-3** (copyright Agile Business Group,
Innoviu, Aion Tech e altri).

USO: solo test in locale sulla mia macchina.
NON ridistribuire, NON committare in altri repo (odoo/enterprise/import-intelligente).

Copiati il 2026-07-22.

## Copertura (55 XML)
- TipoDocumento: TD01 x46, TD04 x2, TD06 x2, TD17 x2, TD07 x1
- Natura: N1, N2, N2.2, N4
- Feature utili non presenti nel nostro dataset generato:
  - p7m firmati: binario, base64, e IT05979361218_fake.xml.p7m (2 byte, corrotto)
  - Allegati (con test.png dentro)
  - ScontoMaggiorazione (10), Arrotondamento (5), DatiBollo, DatiTrasporto (9),
    DatiOrdineAcquisto (8), AltriDatiGestionali (4)
  - XML malformati / URI rotti (IT02780790107_11004_xml_doctor.xml)

Nota: alcune partite IVA sembrano reali; solo ZGEXQROO37831_anonimizzata.xml è marcata anonimizzata.

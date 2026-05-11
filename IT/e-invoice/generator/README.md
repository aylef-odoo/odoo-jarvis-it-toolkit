# 🛠️ SDI XML Generator

A self-contained browser tool to generate SDI (electronic invoice) test XMLs for Odoo. No build step, no install — just open `index.html` in any modern browser.

## 🚀 How to use

1. Open `index.html` in your browser (double-click the file, or `file:///.../index.html`).
2. Fill in the supplier (*Cedente/Prestatore*), customer (*Cessionario/Committente*), and invoice line fields.
3. Click **Download XML** to save the generated file.
4. Import it into Odoo via **Invoicing > Vendors > Bills > Upload**.

## ✨ Features

- **Active / Passive modes** — generate either a customer invoice (Active) or a vendor bill (Passive).
- **Magic fill buttons** — pre-fill seller, buyer, or invoice lines with realistic Italian sample data (uses top 19 Italian companies with real VAT numbers).
- **Multiple document types** — supports the most common SDI codes:
  - `TD01` Invoice • `TD02` Advance/Down payment • `TD04` Credit note • `TD05` Debit note
  - `TD06` Fee • `TD16` Internal reverse charge integration • `TD24` Deferred invoice
- **Tax regimes** — `RF01` (ordinary), `RF02`, `RF04`, `RF19` (forfettario), and others.
- **Transmission format** — generates `FPR12` (private) XML, the most common case for B2B/B2C testing.

## 📐 Output format

The XML follows the official SDI schema (`fatturapa.gov.it`, version 1.2) and is structured to be imported cleanly by Odoo's `l10n_it_edi` module.

Filename convention: `<CountryCode><VATNumber>_<ProgressiveNumber>.xml`
(e.g. `IT01234560157_00001.xml`).

## 🐛 Known notes

- The tool runs entirely client-side — nothing is sent to a server.
- If Odoo rejects the import, check that the **Codice Destinatario** is set correctly (`0000000` for private consumers, `XXXXXXX` 7-char code for businesses, `M5UXCR1` etc. for PA).

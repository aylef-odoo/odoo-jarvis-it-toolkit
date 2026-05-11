# 🇮🇹 Italy — Electronic Invoicing (SDI)

Sample XML files and a browser-based generator to test the Italian electronic invoicing flow (**SDI** — *Sistema di Interscambio*).

## 📂 What's in this folder

| Path | What it is |
|------|------------|
| [`samples/`](./samples/) | Ready-made SDI XML invoices you can use directly. |
| [`generator/`](./generator/) | An HTML tool to generate custom SDI test XMLs in your browser. |

## 📦 Samples

The `samples/` folder contains pre-built SDI-compliant XML invoices. Use them to:

- Test the **incoming e-invoice** flow in Odoo (upload as a vendor bill via SDI).
- Inspect the expected XML structure (header, transmission data, supplier, customer, lines, totals).

### Usage in Odoo

1. Go to **Invoicing > Vendors > Bills**.
2. Use the **Upload** action and select the XML file.
3. Odoo will parse the XML and create a draft bill.

> The filename convention is `<CountryCode><VATNumber>_<ProgressiveNumber>.xml` (e.g. `IT01234560157_00001.xml`).

## 🛠️ Generator

The `generator/` folder is a self-contained HTML tool — no build, no install. Just open it in a browser. See its [README](./generator/README.md) for details.

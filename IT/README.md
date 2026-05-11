# 🇮🇹 Italy — Odoo Sample Data

Sample data and tooling to test the Italian Odoo localization (`l10n_it`) end-to-end: accounting demo records, electronic invoicing (SDI), and CBI payment batches.

## 📋 Prerequisites

* Odoo (version 19 or higher recommended).
* **Accounting** or **Invoicing** app installed.
* Italian localization package installed (`l10n_it`), which generates the standard chart of accounts and VAT registers.

## 📂 Sections

| Folder | What's inside | When to use it |
|--------|---------------|----------------|
| [`demo-data/`](./demo-data/) | CSVs to bulk-import contacts, banks, invoices, and bills | Populate a blank Odoo DB with realistic Italian accounting records (B2B, B2C, PA, EU/Extra-EU, Split Payment, Reverse Charge, Exports). |
| [`e-invoice/`](./e-invoice/) | SDI XML samples + a browser-based XML generator | Test electronic invoice import or generate custom test XMLs. |
| [`cbi/`](./cbi/) | CBI / SEPA payment batch XML examples | Inspect or test the payment-batch format Odoo generates for Italian banks. |

Open each folder's `README.md` for step-by-step instructions.

## 🗺️ At a glance

```
IT/
├── demo-data/        # CSV demo records → bulk import into Odoo
├── e-invoice/        # XML SDI samples + HTML generator tool
│   ├── samples/
│   └── generator/
└── cbi/              # CBI payment batch XML examples
```

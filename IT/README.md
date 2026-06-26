# 🇮🇹 Italy — Odoo Jarvis IT Toolkit

Sample data and tooling to test the Italian Odoo localization (`l10n_it`) end-to-end: accounting demo records, electronic invoicing (SDI), CBI payment batches, and small browser-based helpers.

## 📋 Prerequisites

* Odoo (version 19 or higher recommended).
* **Accounting** or **Invoicing** app installed.
* Italian localization package installed (`l10n_it`), which generates the standard chart of accounts and VAT registers.

## 📂 Sections

> 🌐 **Live tools (no install):** [SDI e-invoice XML generator](https://aylef-odoo.github.io/odoo-jarvis-it-toolkit/IT/e-invoice/generator/) · [Province → `state_id` converter](https://aylef-odoo.github.io/odoo-jarvis-it-toolkit/IT/state-id-converter/) · [Domain filter builder](https://aylef-odoo.github.io/odoo-jarvis-it-toolkit/IT/domain-filter/) — or browse from the [toolkit home](https://aylef-odoo.github.io/odoo-jarvis-it-toolkit/).

| Folder | What's inside | When to use it |
|--------|---------------|----------------|
| [`demo-data/`](./demo-data/) | CSVs to bulk-import contacts, banks, invoices, and bills | Populate a blank Odoo DB with realistic Italian accounting records (B2B, B2C, PA, EU/Extra-EU, Split Payment, Reverse Charge, Exports). |
| [`e-invoice/`](./e-invoice/) | SDI XML samples + a browser-based XML generator | Test electronic invoice import or generate custom test XMLs. |
| [`cbi/`](./cbi/) | CBI / SEPA payment batch XML examples | Inspect or test the payment-batch format Odoo generates for Italian banks. |
| [`state-id-converter/`](./state-id-converter/) | Browser tool that maps Italian provinces to `base.state_it_*` external IDs | Prepare a CSV/Excel for import so `state_id` resolves correctly in Odoo. |
| [`domain-filter/`](./domain-filter/) | Browser tool that builds an Odoo domain filter from a list of values | Generate a `["|", ...]` domain (ilike/in/=) to paste into a filter, server action, or `search`. |

Open each folder's `README.md` for step-by-step instructions.

## 🗺️ At a glance

```
IT/
├── demo-data/           # CSV demo records → bulk import into Odoo
├── e-invoice/           # XML SDI samples + HTML generator tool
│   ├── samples/
│   └── generator/
├── cbi/                 # CBI payment batch XML examples
├── state-id-converter/  # Browser tool: province → base.state_it_* external ID
└── domain-filter/       # Browser tool: list of values → Odoo domain filter
```

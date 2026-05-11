# 🇮🇹 Italy — Accounting Demo Data (CSV)

This folder contains CSV files designed to populate a "blank" Odoo database with realistic Italian accounting records.

The data covers various types of master data and documents, including complex scenarios such as **Electronic Invoicing (Fatturazione Elettronica), Split Payment, Reverse Charge (EU, Extra-EU, Domestic), and Exports**.

## 📋 Prerequisites

* Odoo (version 19 or higher recommended).
* **Accounting** or **Invoicing** app installed.
* Italian localization package installed (`l10n_it`), which generates the standard chart of accounts and VAT registers.

## 📦 Files in this folder

| File | Content |
|------|---------|
| `customers_all_cases.csv` | B2B, B2C, Public Administration (PA), EU and Extra-EU partners — complete with VAT number, Tax Code (Codice Fiscale), Destination Code (SDI), and Payment Terms. |
| `banks_accounts.csv` | IBAN coordinates associated with the contacts above. |
| `invoices.csv` | Customer invoices (`out_invoice`). Multiple lines and mixed VAT regimes (22%, Exemptions, Split Payment, Non-Taxable). |
| `bills.csv` | Vendor bills (`in_invoice`). Purchases of goods/services and self-invoices/integrations for Reverse Charge. |

## 🚀 Mandatory Import Order

In Odoo, database relations are crucial. The files must be imported strictly in this order to allow the system to link the data correctly:

1. **`customers_all_cases.csv`**
   * **Menu:** Contacts > Favorites > Import records

2. **`banks_accounts.csv`**
   * **Menu:** Contacts > Configuration > Bank Accounts > Import records

3. **`invoices.csv`**
   * **Menu:** Invoicing > Customers > Invoices > Import records

4. **`bills.csv`**
   * **Menu:** Invoicing > Vendors > Bills > Import records

## ⚠️ Important Notes for Importing

### 1. The `move_type` field in Invoices
During the import of files 3 and 4, if Odoo attempts to automatically map the `move_type` column to "Origin Document Type", **cancel the mapping (by clicking the X)**. Odoo will automatically recognize the correct document type based on the menu you are currently in.

### 2. Tax Management (External IDs)
To avoid the classic Odoo error *"Found multiple matches for value..."* (usually caused by sales and purchase taxes sharing the exact same name, e.g., "22%"), the invoice files use **External IDs** instead of plain text.
* The CSV column is named `invoice_line_ids/tax_ids/id`.
* In the Odoo import interface, make sure it is mapped to: **Invoice lines / Taxes / External ID**.

**Beware of the Company prefix:** The external IDs in these files use the standard `account.1_` prefix (e.g., `account.1_22v`). The number `1` represents the ID of the first company created in the database. If you are working on a multi-company database or your company has a different ID, the codes might vary (e.g., `account.2_22v`). In that case, export the taxes from *Configuration > Taxes* to find the exact prefix for your specific instance.

### 3. Document Confirmation (From Draft to Posted)
Odoo always imports accounting documents in **Draft** state to avoid gaps in numbering.
Once the invoices are imported, select all of them from the list view (using the top-left checkbox) and use the **Confirm** action. Odoo will assign each one its sequential protocol number and post them to the journal.

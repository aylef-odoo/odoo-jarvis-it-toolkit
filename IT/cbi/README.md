# 🇮🇹 Italy — CBI Payment Batches

Example XML files in the **CBI** format (*Customer to Bank Interbank*) — the standard Italian banks use to receive SEPA payment batches from their corporate clients.

These files show the format Odoo generates when you export supplier payments for transmission to the bank.

## 📦 Files in this folder

| File | What it shows |
|------|---------------|
| `cbi_example.xml` | Basic CBI/SEPA payment batch (`CBIPaymentRequest`) — single payment block, multiple transactions. |
| `cbi_example_v2.xml` | Extended example with additional fields and edge cases. |

## 🧠 Background

- **CBI** (*Consorzio CBI*) is the Italian inter-bank consortium that defines the XML messages used by Italian banks.
- The CBI payment-request schema (`CBIPaymentRequest.00.04.01`) is built on top of the ISO 20022 SEPA standard (`pain.001`).
- Italian Odoo modules such as `l10n_it_sepa` and `account_sepa` generate these XML files when running batch payments.

## 🚀 Usage

These files are **reference samples**, not files to import into Odoo. Use them to:

1. **Verify Odoo's output** — compare an XML you exported from Odoo against these samples to spot structural differences.
2. **Understand the schema** — see how `GrpHdr`, `PmtInf`, `CdtTrfTxInf`, etc. are populated for the Italian flavor.
3. **Test bank integration** — feed them into your bank's home-banking portal sandbox to verify acceptance.

## 🔗 Related Odoo modules

- `account_sepa` — generates SEPA Credit Transfer (`pain.001`) XML.
- `l10n_it_sepa` — Italian extensions (CBI-specific fields and structure).

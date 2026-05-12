# 🇮🇹 Province → `state_id/id` Converter

Browser-based helper to translate Italian province values into Odoo's native external IDs (`base.state_it_*`), so a CSV or Excel can be imported into `res.partner` (or any model with a `state_id` field) without manual lookups.

## ✨ What it does

* Reads a `.csv`, `.xlsx`, or `.xls` file entirely in the browser (no upload).
* Auto-detects the province column (accepts headers like `provincia`, `province`, `prov`, `pr`, `state`).
* Recognizes both **two-letter codes** (`MI`, `RM`, `TO`…) and **full names** (`Milano`, `Roma`, `Torino`…).
* Outputs a new file where the province column is replaced by the matching `base.state_it_xx` external ID, ready for Odoo's standard import.

## 🚀 Usage

1. Open [`index.html`](./index.html) in any modern browser (double-click or serve locally — no build step).
2. Drag-and-drop your file, or click the dropzone.
3. Download the converted file from the results panel.

## 📌 Notes

* `base.state_it_*` are the external IDs shipped by Odoo's `base` module — no extra import of states is required.
* Rows with unrecognized values are flagged in the results so you can fix the source before importing.
* Processing happens 100% client-side; the file never leaves the browser.

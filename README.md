# Odoo Jarvis IT Toolkit 🌍

A growing collection of **sample data, format examples, and small browser-based tools** to help test, demo, and prepare data for country-specific Odoo localizations.

The repository is organized **by country**. Each country folder contains its own demo data, format samples (e.g. e-invoicing, payment batches), and any localization-specific helper tools.

## 📦 Repository contents

| Path | What it is |
|------|------------|
| [`IT/`](./IT/) | 🇮🇹 Italy — accounting demo data, SDI samples + XML generator, CBI payment examples, province → `state_id` converter |
| [`agents/`](./agents/) | 🤖 AI skill for [Google Gemini](https://gemini.google.com) — ask the assistant how any Odoo feature works and get a functional report. Runs as a no-install **Gem** in the browser, or via the **Gemini CLI** to save reports to files |

Each country folder has its own `README.md` with an overview and links to each section. The `agents/` folder has its own `README.md` explaining the one skill and its two ways to run: a no-install **Gemini Gem** in the browser (the easiest start), or the **Gemini CLI** (installs the skill with `gemini skills install` and saves reports to files).

## 🚀 Quick start

**Testing localization data & tools:**
1. Pick the country folder for the localization you're testing (currently only `IT/`).
2. Open its `README.md` for an overview and links to data sets and tools.
3. Follow the per-section guides for import steps, warnings, and usage tips.

**Want the AI assistant that explains how Odoo works (no coding needed)?**
Head to [`agents/`](./agents/) — its README walks you through both options. The easiest start is a **Gemini Gem**: paste the ready-made instructions into a browser Gem (zero install). Prefer reports saved to files? Use the **Gemini CLI**, which loads the skill with `gemini skills install`.

## 🧰 What's inside, in two categories

* **Sample data** — CSV files designed for Odoo's standard bulk import (contacts, banks, invoices, bills, etc.).
* **Tools** — single-file HTML utilities you can open directly in a browser (no build step, no upload — everything runs locally). Examples: the Italian SDI XML generator, the province → `state_id` converter.

When a tool is **country-agnostic**, it will live under a top-level `tools/` folder (added when the first one lands). Country-specific tools stay under their country folder.

## 🤝 Contributing

Pull requests adding new countries, scenarios, tools, or fixes are welcome. When adding a new country, follow the same structure:

```
<COUNTRY_CODE>/
├── README.md           # country overview + links
├── demo-data/          # CSVs for bulk import
└── ...                 # localization-specific samples and tools
```

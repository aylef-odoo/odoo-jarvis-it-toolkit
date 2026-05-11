# Odoo Sample Data 🌍

A collection of realistic sample data, format examples, and tools to help test and demo **Odoo** with country-specific localizations.

The repository is organized **by country**. Each country folder contains demo data for bulk import, plus any localization-specific assets (electronic invoicing, payment formats, etc.).

## 📦 Repository contents

| Path | What it is |
|------|------------|
| [`IT/`](./IT/) | 🇮🇹 Italy — accounting demo data, SDI samples + generator, CBI payment examples |

Each country folder has its own `README.md` explaining what's included and how to use it.

## 🚀 Quick start

1. Pick the country folder for the localization you're testing (currently only `IT/`).
2. Open its `README.md` for an overview and links to each section.
3. Follow the per-section guides for import steps, warnings, and usage tips.

## 🤝 Contributing

Pull requests adding new countries, scenarios, or fixes are welcome. When adding a new country, follow the same structure:

```
<COUNTRY_CODE>/
├── README.md           # country overview + links
├── demo-data/          # CSVs for bulk import
└── ...                 # any localization-specific assets
```

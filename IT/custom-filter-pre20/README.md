# 🌳 Odoo Domain Builder (pre-v20)

Browser-based visual query builder for nested Odoo domains with AND / OR logic, automatically computing the Polish prefix notation (`"&"`, `"|"`) required by Odoo versions prior to v20.

## ✨ What it does

* **Visual nesting**: Add conditions and nested groups with intuitive AND / OR switches.
* **Automatic prefix operators**: In Odoo (< v20), domains use Polish prefix notation (`['&', ...]` or `['|', ...]`). The tool calculates the exact number and positions of operators.
* **Type-aware formatting**: Automatically detects numbers, booleans (`True`/`False`), strings, and lists (`in` / `not in` operators with comma-separated values).
* **Syntax highlighting**: Live syntax-highlighted domain preview matching the toolkit theme.
* **One-click copy**: Copy the formatted domain directly to your clipboard for use in server actions, filters, or Python code.
* **100% Client-side**: Runs entirely in the browser with zero dependencies, zero build steps, and zero server roundtrips.

## 🚀 Usage

1. Open [`index.html`](./index.html) in any modern browser.
2. Toggle groups between **AND** and **OR**.
3. Fill in field names, comparison operators, and values.
4. Click **+ condition** or **+ group** to build complex filter trees.
5. Click **Copy** to copy the generated domain.

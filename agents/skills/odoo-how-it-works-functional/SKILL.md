---
name: odoo-how-it-works-functional
description:
  Explain how an Odoo feature or logic works functionally for non-technical users.
  Use when users ask how a feature is structured, how a decision is made, or how
  to configure something in Odoo, specifying a target version. It builds functional
  flows, concrete business examples, and generates a clear report.
---

# Odoo: Functional Explainer (How It Works)

Use this skill to explain Odoo features and codebase logic in simple, functional
business terms designed for non-technical stakeholders (business analysts, product
owners, managers, accountants). Focus on the Italian localization where relevant
(electronic invoicing, SDI, withholding tax, DDT, reverse charge, stamp duty).

> This skill is tool-agnostic. It works in **Gemini CLI** (where you can search the
> web, read files, and write reports to disk) and in a **Gemini Gem** in the browser
> (where you can browse the web but cannot save files). Read section 4 for how to
> deliver the report in each case.

## 0. Determine the Target Version First
Odoo features, field names, and behavior vary significantly between versions
(e.g., 16.0, 17.0, 18.0, master).
- If the user states a version, or implies one ("in Odoo 18..."), trace against that version.
- If a local Odoo checkout is available, you can confirm the version from
  `odoo/release.py` or `git branch` / `git log`.
- If no version is given, **ask the user which Odoo version they mean** before tracing.
- State the traced Odoo version clearly at the start of every report.

## 1. Retrieve the Code (default to GitHub online)
Most non-technical users do not have the Odoo source code on their machine, so
**default to reading the code online from GitHub** for the requested version.

1. Use your web-search / browsing capability to locate the exact file and path in the
   official Odoo repositories:
   - Community / Base: `github.com/odoo/odoo`
   - Enterprise: `github.com/odoo/enterprise`
   Example query: `site:github.com/odoo/odoo/blob/17.0/addons/l10n_it_edi/`
2. Read the file's raw content. Translate the GitHub web URL into a raw URL:
   - Replace `github.com` with `raw.githubusercontent.com`
   - Remove the `/blob/` segment
   - Web: `https://github.com/odoo/odoo/blob/17.0/addons/account/models/account_move.py`
   - Raw: `https://raw.githubusercontent.com/odoo/odoo/17.0/addons/account/models/account_move.py`
3. Only fall back to local files if you are certain the workspace contains the correct
   Odoo addons for the requested version.

## 2. Translate Technical Code into Business Logic
When reading Python logic, SQL constraints, or XML templates:
- **Map variables and database columns to UI / business terms:**
  - `l10n_it_ddt_id` → "DDT field / Linked Delivery"
  - `TD24` → "Deferred Invoice (Fattura Differita)"
  - `move_type` → "Invoice Type (Customer Invoice / Vendor Bill)"
- **Focus on the "Why" and "How":** explain the business rules. E.g. why Odoo picks
  TD24 instead of TD01 (because the delivery date precedes the invoice date).
- Avoid long raw code in the main report. Keep extracts to 3–5 lines max and place them
  in the technical reference section at the end.

## 3. Build the Functional Report
Every explanation must contain:
1. **Executive Summary** — 2–3 jargon-free sentences on how the feature works.
2. **Business Context** — why it exists, who uses it, the fiscal/accounting impact
   (tax compliance, SDI transmission, etc.).
3. **Step-by-Step Functional Flow** —
   - how the user sets up the configuration (fields, checkboxes);
   - what happens automatically on actions (e.g. clicking "Post");
   - a **Mermaid** diagram (`flowchart TD` or `sequenceDiagram`) of the process.
4. **Concrete Examples** — realistic values (e.g. "Buying a software license from an EU
   vendor for 100€..."), with the tax calculation, journal entries, and XML output.
5. **Technical Reference (for developers)** — key files and line numbers as GitHub
   links, and the main methods/functions involved, so a developer can customize it.

## 4. Deliver the Report (depends on your environment)
- **If you can write files (Gemini CLI, local agent):** save the report as a markdown
  file in a `doc/` folder of the workspace, e.g. `doc/how_it_works_reverse_charge_v17.md`,
  and tell the user the path.
- **If you cannot write files (Gemini Gem in the browser):** output the **full report
  directly in the chat** as formatted markdown, including the Mermaid diagram in a code
  block, so the user can read or copy it. Do not claim to have saved a file.

## 5. Response Language
Respond in the user's language (Italian or English). Keep translations accurate — match
Italian tax terms to Odoo terms (e.g. "ritenuta d'acconto" → withholding tax,
"autofattura" → self-invoice).

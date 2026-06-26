# Agents & Skills for Google Gemini 🤖

This section bundles an **AI skill for Google Gemini** that explains how Odoo works in
plain business language — no developer code, no programming required.

It is built for **non-technical users** (business analysts, product owners, managers,
accountants) who need to understand the inner logic of Odoo, especially the Italian
localization (electronic invoicing, SDI, withholding taxes, DDT, reverse charge), and
get a clear functional report to share with their developers.

With the **Odoo Functional Explainer** you can ask how any logic or automation in Odoo
works (tax calculation, DDT tracking, self-billing, etc.) and receive a clean functional
report complete with practical examples, diagrams, and developer-ready references.

There is **one skill**, used in two ways:

| Way | Where it runs | Install needed | Best for |
|-----|---------------|----------------|----------|
| **Gemini CLI** (primary) | Your terminal | Node.js + a CLI | The full skill: reads Odoo on GitHub and **saves reports to files**. |
| **Gemini Gem** (fallback) | gemini.google.com (browser) | **None** | People without the CLI — same logic, answers come back in the chat. |

> A **skill** is a small set of instructions that teaches the AI assistant how to behave
> for a specific job. You set it up once, then it works automatically whenever your
> request matches what it is for. The **Gem** is the same skill pasted into the browser
> for people who can't (or don't want to) install the CLI.

---

## 📦 What's inside

| Path | What it is |
|------|------------|
| [`skills/odoo-how-it-works-functional/SKILL.md`](./skills/odoo-how-it-works-functional/SKILL.md) | The **skill** in Agent Skills format — what the Gemini CLI loads. |
| [`skills/odoo-how-it-works-functional/GEM.md`](./skills/odoo-how-it-works-functional/GEM.md) | The same instructions, **paste-ready** for a browser Gem (the fallback). |

Everything lives under the one skill folder, so the CLI and the Gem stay in sync.

---

# Primary — Gemini CLI 💻

The **Gemini CLI** is a free, open-source command-line assistant from Google. It loads the
skill directly and, because it runs on your computer, it can **save each report as a
markdown file** in a `doc/` folder.

### 1. Install the Gemini CLI and the skill

Install the CLI (needs **Node.js / npm**):

```bash
npm install -g @google/gemini-cli
```

Then add the skill straight from this repository — the CLI installs it for you:

```bash
gemini skills install https://github.com/aylef-odoo/odoo-jarvis-it-toolkit
```

> Replace the URL with this repository's address. The CLI also discovers any skill placed
> in `~/.gemini/skills/`, so you can instead copy the
> [`skills/odoo-how-it-works-functional/`](./skills/odoo-how-it-works-functional/) folder
> there by hand.

### 2. Set up your workspace (no need to clone Odoo!)

> [!IMPORTANT]
> **You do not need to clone the 10 GB of Odoo source code.**
> The skill reads the code directly from GitHub in real time, for any Odoo version.

1. Create an empty folder for your reports (e.g. `odoo-explainer` in your Home).
2. Open a terminal **in that folder** and run `gemini`.
3. Sign in with your Google account when prompted.

### 3. Ask your question

Describe what you want to understand, always specifying:

1. **The Odoo feature or field** you want to understand.
2. **The Odoo version** (e.g. 16.0, 17.0, 18.0, or master). If you forget, it will ask.

The skill activates automatically when your question matches an Odoo functional explanation.

> [!TIP]
> **Case 1: Deferred (TD24) vs immediate (TD01) invoices**
> *"Can you explain how Odoo 17.0 decides whether an invoice should be sent to SDI with
> code TD24 (deferred invoice) or TD01 (immediate invoice)?"*

> [!TIP]
> **Case 2: Reverse charge and self-billing**
> *"How does the automatic generation of reverse-charge self-invoices (e.g. TD17 or TD18)
> work in Odoo 18.0? Which tax configurations are needed?"*

> [!TIP]
> **Case 3: Stamp duty calculation**
> *"In Odoo 16.0, when is the DatiBollo block added to the electronic invoice XML and how
> is the 2€ amount calculated?"*

### 4. Read and use the report

The CLI saves a markdown report into the `doc/` folder of your workspace (e.g.
`doc/how_it_works_reverse_charge_v17.md`) and tells you the path. See
[What the report contains](#-what-the-report-contains) below.

---

# Fallback — Gemini Gem (no install) 🌐

For people **without the Gemini CLI**, the same skill runs as a **Gem** — a custom version
of Gemini you build in your browser. Nothing to install, just a Google account. The only
difference: a Gem can't save files, so it writes the report **directly in the chat**.

### 1. Create the Gem

1. Go to **https://gemini.google.com/gems/create** (or open
   [gemini.google.com](https://gemini.google.com) → **Gems** → **New Gem**).
2. **Name** it, e.g. `Odoo Functional Explainer`.
3. Open [`skills/odoo-how-it-works-functional/GEM.md`](./skills/odoo-how-it-works-functional/GEM.md),
   copy **everything inside the grey instructions box**, and paste it into the Gem's
   **Instructions** field.
4. Click **Save**.

The Gem now appears in the Gemini web app, the mobile app, and the Gemini side panel in
Google Workspace.

### 2. Ask your question

Open a chat with your Gem and ask as you would in the CLI (same example prompts above),
remembering to state the **Odoo version**. The Gem reads the real Odoo source on GitHub and
writes the report straight into the chat.

---

## 📄 What the report contains

| Section | Content | Why it helps you |
| :--- | :--- | :--- |
| **Executive Summary** | A 2–3 sentence jargon-free explanation. | Grasp the overall business logic instantly. |
| **Business Context** | Why the feature exists and its fiscal/regulatory impact. | Provides the business rationale and the tax rules applied. |
| **Functional Flow** | Step-by-step description of what the user does and what the system does behind the scenes, with a **Mermaid** diagram. | Know exactly how to configure Odoo or train colleagues. |
| **Concrete Examples** | A numeric example with real values (tax calculation, journal entries, XML output). | Check whether the calculation matches business expectations. |
| **Technical References** | A table with source files, line numbers, and Python functions. | **The part to send to developers** for changes or bug fixing. |

---

## ❓ Which one should I use?

- **Have a terminal and want reports saved as files?** → **Gemini CLI** (primary).
- **No CLI, just want answers in the browser?** → **Gemini Gem** (fallback).

Both use the exact same logic — only where it runs and how the report is delivered differ.

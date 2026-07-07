# 🇮🇹 Ferie Odoo → XML movimenti SD Worx

Browser tool that turns an Odoo **`hr.leave` export** (the *Ferie / Time Off* list, CSV or XLSX) into the **`<Fornitura>` XML** consumed by SD Worx Italy, matching the layout the `l10n_it_hr_payroll_sd_worx` module produces.

## ✨ What it does

* Reads a `.csv` or `.xlsx` file **entirely in the browser** (no upload, no external library: XLSX is unzipped natively via `DecompressionStream`).
* Auto-detects the columns `Dipendente`, `Tipologia ferie`, `Data inizio`, `Data fine`, `Richiesto`, `Stato` (remappable).
* Normalizes the messy `Richiesto` duration formats: `1:30 hours`, `2:00 ore`, `1 days`, `1 giorno/i`, `0.5 days`.
* **Expands multi-day leaves** into one `<Movimento>` per working day (weekends optionally skipped), e.g. a 14-day sick leave becomes 14 daily 8h movements; `16:00 ore` over two days becomes 8h + 8h.
* Fills the codes the leave export does **not** contain by pasting the Zucchetti `Ele DIP` roster: employee code (`CodDipendenteUfficiale`) matched by name and company code (`CodAziendaUfficiale`) read straight from the roster. The leave-type → justification code (`CodGiustificativo*`) is pre-filled with sensible guesses in an editable table.
* Groups every movement under its `<Dipendente>` and outputs a downloadable XML.

## 🧭 Output layout

```xml
<Fornitura>
  <Dipendente CodAziendaUfficiale="000009" CodDipendenteUfficiale="0000001">
    <Movimenti GenerazioneAutomaticaDaTeorico="N">
      <Movimento>
        <CodGiustificativoRilPres>FER</CodGiustificativoRilPres>
        <CodGiustificativoUfficiale>FER</CodGiustificativoUfficiale>
        <Data>2026-06-09</Data>
        <NumOre>8</NumOre>
        <NumMinuti>30</NumMinuti> <!-- only when > 0 -->
      </Movimento>
    </Movimenti>
  </Dipendente>
</Fornitura>
```

Field origins (same mapping as the Odoo module):

| XML | Source |
|-----|--------|
| `CodAziendaUfficiale` | company `external_code` (entered once in the tool) |
| `CodDipendenteUfficiale` | employee `external_code` (mapped per employee) |
| `CodGiustificativoRilPres` / `Ufficiale` | `work_entry_type.external_code` (mapped per leave type) |
| `Data` | leave day, `YYYY-MM-DD` |
| `NumOre` / `NumMinuti` | duration split into whole hours / remainder minutes |

## 🚀 Usage

1. In Odoo, export the *Time Off* list (`hr.leave`) with the columns above to CSV or XLSX.
2. Open [`index.html`](./index.html) in any modern browser (double-click, or use the live link below).
3. Paste the Zucchetti **`Ele DIP`** roster export into the big text box in *Mappa i dipendenti* and press **Abbina automaticamente**: employee codes are matched by name (accent/order insensitive) and the **company code** is filled in automatically. Fill any leftover employee or justification code by hand (red = missing).
4. Set **hours/day** and, if needed, the reference **period**, then press **Genera XML**, review the summary and warnings, and **Scarica .xml**.

### Employee name matching

The leave file only gives `Name Surname (login)`; the `Ele DIP` export gives separate `Cognome` / `Nome` columns plus the SD Worx `Dipendente` code. The tool matches them by normalizing both sides (lowercase, accents and apostrophes stripped, e.g. `Cassarà` ↔ `CASSARA'`) and comparing the name as an **unordered token set**, so `Adriano Veroux` matches `VEROUX` + `ADRIANO`. Unmatched names stay flagged for manual entry. A headerless subset (just the three columns) also works.

## 📌 Notes

* The justification codes are pre-filled with reasonable guesses (`FER`, `MA`, `T35`…). **The real codes depend on your SD Worx setup — confirm them.** Missing codes are flagged in red; rows whose employee or type has no code are excluded and reported.
* Multi-day expansion is duration-driven: the number of daily movements matches the requested working days, regardless of how the calendar range is spread.
* Processing happens 100% client-side; the file never leaves the browser.
* Reference: the `l10n_it_hr_payroll_sd_worx` enterprise module (`models/hr_payroll_export_sdworx.py`, template `l10n_it_sd_worx_template`).

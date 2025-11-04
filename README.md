# Archivio TFA Sostegno — Indice & Stato

> Repository: `GITHUBTFASOS`  
> Cartella principale rilevata: [`TFA_SOSTEGNO/`](./TFA_SOSTEGNO/) · File: [`.gitattributes`](./.gitattributes)

## Legenda stato
- ✅ completo · 🟡 parziale · 🔴 mancante · 🔎 da verificare

---

## 00_ADMIN_E_ORGANIZZAZIONE — 🟡
- 01_Calendario_e_scadenze — 🔎  
- 02_Checklist_e_Kanban — 🔎  
- 03_Rami_attivi — 🔎  
- 04_Log_revisioni — 🔎  
- 05_LINKS (Start page, .webloc, ecc.) — 🔎  

## 01_PEI_e_Didattica_Speciale (docente: Pastore) — 🟡
- 01_Appunti_lezione — 🔎  
- 02_Slide_e_fonti_docenti — 🔎  
- 03_Normativa_e_riferimenti — 🔎  
- 04_Schede_osservative_e_strumenti — 🔎  
- 05_Esercitazioni_e_compiti — 🔎  
- 06_Sintesi_e_mappe — 🔎  
- 07_Bibliografia_e_citazioni — 🔎  
- 08_Output_pronti_(Word_PDF) — 🔎  
- 09_Backup_versioni — 🔎  

## 02_Metacognizione_e_Cooperative_Learning (Gianfregorio) — 🟡
(stessa sottostruttura standard) — 🔎

## 03_TIC_PNSD_DigComp_DigCompEdu (Papale) — 🟡
(stessa sottostruttura standard) — 🔎

## 04_Disabilità_Sensoriali_e_Intellettive (Olivieri, Cottini) — 🟡
(stessa sottostruttura standard) — 🔎

## 05_Codici_Comunicativi / Gestione_Classe (Papale) — 🟡
(stessa sottostruttura standard) — 🔎

## 06_Legislazione_Scolastica (Cellamare) — 🟡
(stessa sottostruttura standard) — 🔎

## 07_Attività_Motoria_e_Sviluppo_PsicoFisico (Girolami) — 🟡
(stessa sottostruttura standard) — 🔎

## 08_Lingue_Tecniche (Francese · Inglese) — 🟡
(stessa sottostruttura standard) — 🔎

## 09_Didattica_Area_Antropologica (Pastore) — 🟡
(stessa sottostruttura standard) — 🔎

---

## 11_OUTPUT_FINALI — 🟡
- Esami_scritti_(4) — 🔎  
- Elaborati_(Studio_di_caso,_Approfondimento_teorico) — 🔎

## 12_ATTUAZIONE_IN_CLASSE — 🟡
- 01_N.R./  
  - 06a_Italiano — 🔎 · 06b_Matematica — 🔎  
- 02_P.A./  
  - 06a_Italiano — 🔎 · 06b_Matematica — 🔎

---

## TODO immediati
- [ ] Carica/ordina i materiali dentro `TFA_SOSTEGNO/` seguendo le sezioni sopra.  
- [ ] Aggiorna gli **stati** (✅/🟡/🔴) man mano che compili le cartelle.  
- [ ] Aggiungi un `README.md` breve **in ogni materia** con: obiettivi, docenti, indice file.  
- [ ] (Opz.) Attiva **GitHub Pages** per una home pubblica (vedi sotto).

---

## Come tenere tutto aggiornato (workflow consigliato)
1. Lavora in locale nella cartella `TFA_SOSTEGNO/` (stesso albero).  
2. Usa **GitHub Desktop** → *Commit* → *Push* per pubblicare aggiornamenti.  
3. Ogni volta che aggiungi slide/appunti, metti i PDF in `08_Output_pronti_(Word_PDF)` e i sorgenti in `02_Slide…` o `01_Appunti…`.  
4. Per evitare confusione: niente spazi doppi nei nomi, usa `_` e cognomi docenti nel nome cartella.

---

## (Opzionale) Home pubblica — GitHub Pages
Crea un file `index.html` in root con link rapidi:

```html
<!doctype html><meta charset="utf-8">
<title>Archivio TFA Sostegno</title>
<style>
body{font-family:system-ui;margin:24px;line-height:1.5}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
.card{border:1px solid #e5e5e5;border-radius:12px;padding:14px}
.card h3{margin:0 0 6px}
a{text-decoration:none}
</style>
<h1>Archivio TFA Sostegno</h1>
<div class="grid">
  <div class="card"><h3>Cartella principale</h3><p><a href="./TFA_SOSTEGNO/">Apri TFA_SOSTEGNO ↗</a></p></div>
  <div class="card"><h3>Output finali</h3><p><a href="./TFA_SOSTEGNO/11_OUTPUT_FINALI/">Apri Output ↗</a></p></div>
  <div class="card"><h3>Attuazione in classe</h3><p><a href="./TFA_SOSTEGNO/12_ATTUAZIONE_IN_CLASSE/">Apri N.R. / P.A. ↗</a></p></div>
</div>
<p><small>Aggiorna cartelle e file, poi fai Commit/Push: la pagina si aggiorna.</small></p>

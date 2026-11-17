#!/usr/bin/env python3
"""Regenerate catalog.qmd from registry without external packages."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parents[1]
with (root/'ARTIFACT_REGISTER.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
lines=['---','title: "Katalog 42 Artefak"','---','','> Semua entri awalnya **DRAFT**. Status harus diperbarui setelah review dan uji pengguna.','','| Indeks | ID tetap | Artefak | Tema | Jenis | Prioritas | Tim | Status |','|---|---|---|---|---|---|---|---|']
for r in rows:
 lines.append(f"| {r['index_code']} | {r['id']} | [{r['title']}]({r['file']}) | {r['theme_title']} | {r['type']} | {r['priority']} | {r['owner']} | {r['status']} |")
(root/'catalog.qmd').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('Wrote catalog.qmd for',len(rows),'artifacts')

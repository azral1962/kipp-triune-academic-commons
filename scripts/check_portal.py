#!/usr/bin/env python3
"""Static checks without browser or external Python dependencies."""
from pathlib import Path
import csv
root = Path(__file__).resolve().parents[1]
with (root/'ARTIFACT_REGISTER.csv').open(encoding='utf-8', newline='') as f:
    rows=list(csv.DictReader(f))
issues=[]
html=(root/'portal/index.html').read_text(encoding='utf-8')
js=(root/'portal/assets/app.js').read_text(encoding='utf-8')
for path in ['portal/assets/style.css','portal/assets/app.js','portal/index.html','scripts/build_portal.py']:
    if not (root/path).exists(): issues.append('Missing '+path)
for path in ['assets/artifacts-data.js','assets/app.js','assets/style.css']:
    if path not in html: issues.append('Missing include '+path)
if 'window.KIPP_ARTIFACTS' not in js: issues.append('Catalog does not use generated manifest')
if "encodeURI('learn/'" not in js: issues.append('Artifact links not to Quarto output')
for r in rows:
    if not (root/r['file']).is_file(): issues.append('Missing artifact '+r['file'])
if issues: raise SystemExit('\n'.join(issues))
print(f'PASS: {len(rows)} artifact paths and unified portal bindings')

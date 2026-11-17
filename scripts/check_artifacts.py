#!/usr/bin/env python3
"""Lightweight structural validation; no external packages."""
from pathlib import Path
import csv, re, sys
root=Path(__file__).resolve().parents[1]
with (root/'ARTIFACT_REGISTER.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
errors=[]
if len(rows)!=42:errors.append(f'Expected 42 artifacts, found {len(rows)}')
if len({r['id'] for r in rows})!=len(rows):errors.append('Duplicate artifact IDs')
for r in rows:
 p=root/r['file']
 if not p.is_file():errors.append(f'Missing: {r["file"]}');continue
 s=p.read_text(encoding='utf-8')
 if not s.startswith('---\n'):errors.append(f'No YAML header: {p}')
 for key,value in [('id',r['id']),('priority',r['priority']),('status',r['status']),('type',r['type'])]:
  if not re.search(r'^'+key+r':\s*["\']?'+re.escape(value)+r'["\']?\s*$',s,re.M):errors.append(f'{r["id"]}: invalid {key}')
 for heading in ['Catatan penggunaan AI dan etika','Peer review, uji pengguna, dan refleksi']:
  if heading not in s:errors.append(f'{r["id"]}: missing {heading}')
# Verify hierarchical codes and the navigation references in topic index / learning paths.
for r in rows:
 code=r.get('index_code','')
 parts=code.split('.')
 if len(parts)!=3 or not all(re.fullmatch(r'\d{2}',x) for x in parts):
  errors.append(f'{r["id"]}: missing/invalid index_code {code}')
 else:
  base=f'topics/{parts[0]}-'
  if not r['file'].startswith(base) or not Path(r['file']).name.startswith('-'.join(parts)+'-'):
   errors.append(f'{r["id"]}: filename code does not match index_code')
  parent=root/Path(r['file']).parent.parent/'index.qmd'
  if not parent.exists() or Path(r['file']).name not in parent.read_text(encoding='utf-8'):
   errors.append(f'{r["id"]}: missing link from topic index')
  lp=next((p for p in (root/'learning-paths').glob(f'{parts[0]}-*.qmd')),None)
  if not lp or Path(r['file']).name not in lp.read_text(encoding='utf-8'):
   errors.append(f'{r["id"]}: missing link from learning path')
for r in rows:
 if f'index_code: "{r["index_code"]}"' not in (root/r['file']).read_text(encoding='utf-8'):
  errors.append(f'{r["id"]}: missing index_code in metadata')
for lp in (root/'learning-paths').glob('*.qmd'):
 if lp.name!='index.qmd' and '## Asesmen' not in lp.read_text(encoding='utf-8'):errors.append(f'Missing assessment in {lp.name}')
print(f'Checked {len(rows)} artifacts, {len(list((root/"learning-paths").glob("*.qmd")))-1} learning paths')
if errors:
 print('\n'.join('ERROR: '+e for e in errors));sys.exit(1)
print('PASS: repository scaffolding consistent. DRAFT content still requires human review.')

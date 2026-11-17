#!/usr/bin/env python3
"""Build one deployable static website from ONE source repository.

Build with `quarto render` first; then this script assembles the portal,
rendered learning pages, current register, and downloadable original sources.
"""
import argparse
import csv
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--allow-missing-quarto', action='store_true', help='local preview only')
args = parser.parse_args()
with (ROOT / 'ARTIFACT_REGISTER.csv').open(newline='', encoding='utf-8') as fh:
    records = list(csv.DictReader(fh))
assert len(records) == 42, f'Expected 42 artifacts, got {len(records)}'

output = ROOT / '_public'
if output.exists():
    shutil.rmtree(output)
shutil.copytree(ROOT / 'portal', output)
assets = output / 'assets'
assets.mkdir(exist_ok=True)
(assets / 'artifacts.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(assets / 'artifacts-data.js').write_text('window.KIPP_ARTIFACTS = ' + json.dumps(records, ensure_ascii=False, separators=(',', ':')) + ';\n', encoding='utf-8')

rendered = ROOT / '_site'
if rendered.is_dir() and (rendered / 'index.html').exists():
    shutil.copytree(rendered, output / 'learn', dirs_exist_ok=True)
elif not args.allow_missing_quarto:
    raise SystemExit('ERROR: _site/index.html belum tersedia. Jalankan `quarto render` terlebih dahulu.')
else:
    (output / 'learn').mkdir(exist_ok=True)
    (output / 'learn' / 'index.html').write_text('<!doctype html><html lang="id"><meta charset="utf-8"><title>Quarto belum dibangun</title><p>Jalankan <code>quarto render</code> agar materi belajar tersedia.</p></html>', encoding='utf-8')

# Snapshot of DOCUMENTS generated from same source at build time; never maintained separately.
mirror = output / 'repository'
mirror.mkdir(parents=True, exist_ok=True)
for filename in ['README.md', 'PROJECT_CHARTER.md', 'QUALITY_GATE.md', 'GOVERNANCE.md', 'CONTRIBUTING.md', 'ARTIFACT_REGISTER.csv', 'LICENSE-DECISION.md']:
    shutil.copy2(ROOT / filename, mirror / filename)
for folder in ['docs', 'templates', 'governance']:
    shutil.copytree(ROOT / folder, mirror / folder, dirs_exist_ok=True)

print(f'Published portal: {output}')
print(f'Catalog sourced from registry: {len(records)} entries')
print('Quarto site included:', bool(rendered.is_dir() and (rendered / 'index.html').exists()))

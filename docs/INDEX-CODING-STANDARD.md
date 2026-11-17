# Standar Indeks Hierarkis KIPP Triune Academic Commons

Format kode **TT.JJ.NN**:

- **TT** = nomor tema (01–06)
- **JJ** = jenis artefak (01 Knowledge, 02 Skills, 03 AI Prompts, 04 Case Studies)
- **NN** = nomor urut jenis artefak di tema (01–02 untuk K/S/P; 01 untuk C)

Contoh: `02.03.01` = tema Literatur (02), jenis AI Prompts (03), urutan 01.
Path: `topics/02-literature-research/03-ai-prompts/02-03-01-p-r01.qmd`.

ID lama (`P-R01`) tetap dipertahankan sebagai **ID stabil** pada metadata dan register, agar tugas, diskusi, dan bukti kontribusi terdahulu tetap dapat dikenali. **Kode lokasi** bersifat struktur; **ID stabil** adalah identitas akademik.

| Kode tema | Folder | Kelompok mahasiswa |
|---|---|---|
| 01 | `topics/01-ai-learning/` | Tim 01–02 |
| 02 | `topics/02-literature-research/` | Tim 03–04 |
| 03 | `topics/03-academic-writing/` | Tim 05–06 |
| 04 | `topics/04-coding-data/` | Tim 07–08 |
| 05 | `topics/05-visualization-presentation/` | Tim 09–10 |
| 06 | `topics/06-academic-problem-solving/` | Tim 11–12 |

| Kode jenis | Folder | Artefak |
|---|---|---|
| 01 | `01-knowledge/` | knowledge |
| 02 | `02-skills/` | skills |
| 03 | `03-ai-prompts/` | prompts |
| 04 | `04-case-studies/` | cases |

## Folder standar yang tidak diganti namanya

Beberapa folder tetap bernama standar agar alat dan automasi tidak rusak: `.github/`, `scripts/`, `docs/`, `templates/`, `portal/`, `assets/` (di dalam portal), `learning-paths/`, dan `governance/`. Berkas entry point `index.qmd`, `index.html`, `_quarto.yml`, dan `README.md` juga mengikuti konvensi ekosistemnya. Nama berkas **artefak akademik** semuanya sudah memakai kode.

## Perubahan nama dan tautan

Perubahan nama wajib diikuti pembaruan `ARTIFACT_REGISTER.csv`, link antar `.qmd`, navigasi `_quarto.yml`, dan pemeriksaan `scripts/check_artifacts.py`. Gunakan `git mv` ketika berkas sudah berada dalam repositori Git terkelola; untuk paket migrasi ini, berkas dipindahkan sebelum di-*commit*.

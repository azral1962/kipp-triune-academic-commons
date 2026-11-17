# Mengubah status artefak

Status sumber ada di YAML tiap halaman dan `ARTIFACT_REGISTER.csv`.

1. Setelah review dan uji, ubah `status: draft` menjadi `status: reviewed` pada halaman.
2. Ubah kolom `status` baris ID yang sama pada `ARTIFACT_REGISTER.csv`.
3. Jalankan `python scripts/check_artifacts.py && python scripts/build_catalog.py`.
4. Ajukan PR review dan lampirkan bukti pengujian.

Status yang dibolehkan sebagai konvensi: `draft`, `in-review`, `reviewed`, `needs-revision`. Hindari menjadikan hasil AI sebagai pengganti bukti ilmiah.

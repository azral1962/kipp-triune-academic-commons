# Arsitektur Satu Repositori KIPP

```mermaid
flowchart TB
    A[Mahasiswa mengerjakan artefak dan membuat branch] --> B[Issue dan Pull Request]
    B --> C[Peer review dan pemeriksaan otomatis]
    C --> D{Lolos peninjauan?}
    D -- Belum --> A
    D -- Ya --> E[Merge ke main]
    E --> F[GitHub Actions: validasi dan build]
    F --> G[Quarto: render knowledge, skills, prompts, cases, learning paths]
    F --> H[Portal: katalog dari ARTIFACT_REGISTER.csv]
    G --> I[GitHub Pages: /learn/]
    H --> J[GitHub Pages: /]
```

## Prinsip

- Satu repo sumber; website adalah **hasil build**, bukan proyek dengan konten yang diperbarui manual.
- `ARTIFACT_REGISTER.csv` menentukan 42 entri katalog dan tautan artefak.
- `.qmd` di `topics/` ditampilkan sebagai HTML melalui Quarto di `/learn/`.
- Dokumen `.md` tertentu disalin ke `/repository/` sebagai referensi unduhan saat build.
- Diskusi terjadi di GitHub Discussions; keputusan perubahan melalui Issues/PR.
- Proses build hanya memeriksa struktur teknis. Verifikasi substansi tetap dilakukan mahasiswa dan dosen.

## Daftar verifikasi peluncuran

- [ ] Project Charter disepakati
- [ ] Repositori GitHub dibuat
- [ ] GitHub Pages disetel ke GitHub Actions
- [ ] Discussions diaktifkan
- [ ] Aturan PR dan reviewer lintas tim disetujui
- [ ] Semua 12 tim memiliki akses dan penanggung jawab
- [ ] Lisensi karya disepakati
- [ ] Workflow CI lulus
- [ ] Website publik dapat membuka beranda serta satu artefak Quarto
- [ ] Satu perubahan artefak diuji melalui Pull Request hingga muncul di website

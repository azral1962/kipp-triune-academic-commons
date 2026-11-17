# KIPP Triune Academic Commons — Satu Repositori, Satu Website

**II2100 Komunikasi Interpersonal dan Publik | Pilot AI for Academic Work | 3 minggu | 60+ mahasiswa | 12 tim**

Repositori ini merupakan **satu sumber utama** untuk portal proyek dan karya akademik mahasiswa. Tidak perlu mengubah salinan website terpisah. Perubahan artefak yang disetujui lewat Pull Request akan muncul pada website setelah GitHub Actions menjalankan publikasi.

## Struktur utama

```text
portal/                   Halaman depan website (HTML/CSS/JS)
topics/                   42 artefak akademik siap diisi (6 tema)
learning-paths/           6 alur belajar dan halaman indeks
forum/                    Panduan dan halaman forum
docs/                     Panduan proyek dan panduan Git/GitHub
templates/                Template knowledge, skill, prompt, case, review
assessments/              Rubrik dan panduan showcase
governance/               Tim, pencatatan keputusan
ARTIFACT_REGISTER.csv     Sumber tunggal data katalog artefak
_quarto.yml               Konfigurasi website Quarto
scripts/                  Validasi dan pembentukan website
.github/workflows/        CI review dan deploy GitHub Pages
_site/                    Output sementara Quarto (tidak diedit)
_public/                  Output website final (tidak diedit)
```

**Source of truth:** konten di `topics/`, `learning-paths/`, dan dokumen proyek; daftar artefak berada di `ARTIFACT_REGISTER.csv`. File katalog JSON/JavaScript, HTML Quarto, dan paket yang dipublikasikan dibuat otomatis.

## Memulai sebagai koordinator

1. Buat repository GitHub, unggah/commit seluruh berkas dari folder ini pada branch `main` (bukan folder induk yang berisi repo ini).
2. Pada **Settings → Pages → Build and deployment → Source**, pilih **GitHub Actions**.
3. Pada **Settings → General** aktifkan **Discussions**. Tambahkan tim sebagai kolaborator sesuai kewenangan.
4. Atur **Settings → Branches / Rulesets** agar `main` memerlukan Pull Request dan review. Tambahkan pemeriksaan `Validate source artifacts` jika tersedia.
5. Isi `governance/team-roster.csv`, putuskan lisensi sebelum karya dipublikasikan, dan setujui Project Charter.
6. Buka tab **Actions** lalu jalankan **Publish unified KIPP portal** (atau lakukan commit ke `main`).
7. Alamat website pada GitHub Pages umumnya `https://<pemilik>.github.io/<nama-repo>/`, tetapi ikuti URL yang ditampilkan tab Pages/Actions.

Workflow publikasi menyusun portal HTML dari `portal/`, merender seluruh `.qmd` menjadi halaman web Quarto di `/learn/`, serta menyusun manifest artefak berdasarkan file CSV. Berkas `repository/` di website adalah **salinan dokumen yang dihasilkan saat build** untuk diunduh; bukan repositori sumber kedua.

## Memulai secara lokal

Prasyarat: Git, Python 3.10+, Quarto CLI dari https://quarto.org/docs/get-started/.

```bash
git clone https://github.com/PEMILIK/kipp-triune-academic-commons.git
cd kipp-triune-academic-commons
python scripts/check_artifacts.py
python scripts/check_portal.py
python scripts/build_catalog.py
quarto render
python scripts/build_portal.py
python -m http.server 8000 --directory _public
```

Buka `http://localhost:8000/`. Portal berada di `/`, sementara konten Quarto dapat diakses melalui `/learn/` dan tiap artefak di `/learn/topics/<tema>/<jenis>/<id>.html`.

Jika **Quarto belum terpasang**, pratinjau terbatas halaman depan dapat dibuat menggunakan:

```bash
python scripts/build_portal.py --allow-missing-quarto
python -m http.server 8000 --directory _public
```

Dengan mode ini katalog bisa dibuka, tetapi tautan ke halaman Quarto belum aktif sampai `quarto render` dijalankan. Jangan menggunakan mode ini untuk publikasi akhir.

## Kontribusi mahasiswa

1. Cari ID dan penanggung jawab di `ARTIFACT_REGISTER.csv` atau katalog website.
2. Buat Issue, buat branch, lalu edit satu atau beberapa berkas yang menjadi tugas.
3. Sertakan referensi yang benar, bukti penggunaan, batas AI, dan uji coba sesuai template.
4. Uji dengan `python scripts/check_artifacts.py` dan `python scripts/check_portal.py`.
5. Ajukan Pull Request dan minta reviewer lintas tim.
6. Lakukan revisi; koordinator melakukan merge setelah quality gate terpenuhi.
7. Publikasi otomatis dari `main` akan memperbarui website.

Baca `docs/student-workflow.md`, `CONTRIBUTING.md`, `QUALITY_GATE.md`, dan `PROJECT_CHARTER.md` sebelum berkontribusi.

## Penanda status

- **Draft**: konten awal/kerangka yang belum diuji.
- **In review**: sedang diperiksa rekan.
- **Verified**: diperiksa secara akademik dan diuji pengguna sesuai aturan kelas.

Berkas awal **belum otomatis berstatus verified**. Publikasi teknis tidak berarti pengetahuan akademik sudah benar; tanggung jawab validasi ada pada penulis dan reviewer manusia.

## Alur otomatis

- `.github/workflows/validate.yml`: memeriksa struktur 42 artefak, 6 learning path, konsistensi katalog, dan integrasi portal pada push/PR.
- `.github/workflows/publish.yml`: menjalankan validasi, membangun katalog, merender Quarto, membuat situs terpadu, dan mengirim hasil ke GitHub Pages setiap perubahan masuk ke `main`.
- `scripts/build_portal.py`: menghasilkan `/assets/artifacts.json`, `/assets/artifacts-data.js`, halaman Quarto pada `/learn/`, serta arsip dokumen sumber pada `/repository/` dari folder sumber tunggal.

## Catatan peluncuran

Pengaturan GitHub Pages, Discussions, akses anggota, kebijakan branch, dan lisensi **belum dapat diaktifkan oleh ZIP**; koordinator repositori harus mengaturnya pada akun GitHub. Jangan mempublikasikan data personal, kunci API, transkrip privat, atau berkas tanpa izin.

## Indeks sistematis

Semua 42 berkas artefak menggunakan kode hierarkis `TT.JJ.NN` pada nama file dan kode numerik tema/jenis pada folder. Lihat [standar indeks](docs/INDEX-CODING-STANDARD.md) dan [peta migrasi](docs/INDEX-MIGRATION-MAP.csv). ID lama dipertahankan untuk kompatibilitas.

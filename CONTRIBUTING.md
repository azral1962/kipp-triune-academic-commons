# Panduan Kontribusi

1. Pilih artefak dari `ARTIFACT_REGISTER.csv` berdasarkan peran tim; jangan mengubah ID.
2. Isi template dan semua penanda `[ISI ...]`; pertahankan metadata YAML (`id`, `priority`, `status`, `owner`).
3. Cantumkan sumber asli dan batasan. AI hanya membantu; periksa faktanya.
4. Buat branch `tim-XX/ID-artifact`, misalnya `tim-03/K-R01-review-paper`.
5. Ajukan Pull Request memakai template dan mintalah satu review dari **tim lain**.
6. Perbaiki komentar, tulis bukti uji pengguna, dan ubah status `draft` menjadi `reviewed` setelah disetujui.
7. Koordinator mengintegrasikan PR. Hindari mengunggah data personal, token, API key, file besar dan materi berhak cipta tanpa izin.

## Definisi selesai
Tujuan, pembaca, prasyarat, referensi, demonstrasi yang dapat dijalankan, latihan/asesmen, catatan AI, hasil peer review, dan keterkaitan antarartefak tersedia. Artefak dengan celah tetap berstatus `draft`.

## Kebutuhan metadata
Setiap halaman .qmd memiliki `id`, `title`, `type`, `theme`, `owner`, `priority`, `status`, dan `ai_usage` pada YAML front matter.

## Panduan praktik untuk mahasiswa
Baca `docs/student-workflow.md` untuk langkah dengan browser GitHub, GitHub Desktop, dan terminal, termasuk cara mengirim PR, peer review, dan menangani konflik.

## Sistem kode artefak
Gunakan indeks hierarkis `TT.JJ.NN` pada nama folder dan file serta ID tetap seperti `K-L01` dalam register. Jangan mengganti nama folder sendiri tanpa pembaruan navigasi dan register. Lihat [standar indeks](docs/INDEX-CODING-STANDARD.md).

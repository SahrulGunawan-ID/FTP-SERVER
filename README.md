# BUILD TEST
[![Generate Provenance](https://github.com/SahrulGunawan-ID/FTP-SERVER/actions/workflows/generate-provenance.yml/badge.svg?branch=main&event=push)](https://github.com/SahrulGunawan-ID/FTP-SERVER/actions/workflows/generate-provenance.yml)

```markdown
# FTP-SERVER

Server FTP yang dikonfigurasi menggunakan `pyftpdlib` untuk memungkinkan pengguna mengunggah, mengunduh, dan mengedit file dengan mudah. Proyek ini menyediakan dua pengguna: `admin` dan `guest`, dengan izin penuh untuk admin dan akses tanpa autentikasi untuk guest.

## Fitur

- Pengguna `admin` dengan autentikasi (username: `admin`, password: `admin`).
- Pengguna `guest` tanpa autentikasi.
- Izin penuh untuk mengunggah, mengunduh, dan mengedit file.
- Notifikasi koneksi dan pemutusan pengguna.
- Dukungan untuk direktori pengguna yang disesuaikan.

## Struktur Direktori

```
FTP-SERVER/
├── Admin
├── Guest
└── ftp_server.py
```

- `Admin`: Direktori untuk pengguna `admin`.
- `Guest`: Direktori untuk pengguna `guest`.
- `ftp_server.py`: Skrip Python untuk menjalankan server FTP.

## Persyaratan

- Python 3.6 atau lebih baru
- `pyftpdlib`

## Instalasi

1. **Clone Repository**
   ```sh
   git clone https://github.com/SahrulGunawan-ID/FTP-SERVER.git
   cd FTP-SERVER
   ```

2. **Instal `pyftpdlib`**
   ```sh
   pip install pyftpdlib
   ```

3. **Buat Direktori Pengguna**
   ```sh
   mkdir -p /sdcard/FTP-SERVER/Admin
   mkdir -p /sdcard/FTP-SERVER/Guest
   ```

## Penggunaan

1. **Jalankan Server FTP**
   ```sh
   python ftp_server.py
   ```

2. **Notifikasi Server**
   Saat server berjalan, Anda akan melihat pesan berikut:
   ```
   [✓] Running on 192.168.43.1:8022
   [+] User 2
   [+] New connection from <IP>:<Port>
   [-] Disconnected from <IP>:<Port>
   ```

3. **Mengakses Server FTP**
   - **Admin**: Login menggunakan username `admin` dan password `admin`.
   - **Guest**: Akses tanpa autentikasi.

## Kontak

Jika Anda memiliki pertanyaan atau masalah, silakan buka issue di [repo ini](https://github.com/SahrulGunawan-ID/FTP-SERVER/).

Terima kasih telah menggunakan FTP-SERVER! 🚀

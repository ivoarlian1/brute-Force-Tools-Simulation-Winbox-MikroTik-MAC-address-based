# Simulasi Brute Force Winbox via MAC (Hanya untuk Lab Edukasi)

> ⚠️ **HANYA UNTUK TUJUAN EDUKASI**  
> Alat ini dibuat **khusus untuk digunakan di lab pribadi** dan **kepentingan pembelajaran keamanan jaringan**.  
> Jangan gunakan pada perangkat atau jaringan tanpa izin. Penggunaan tanpa izin adalah **ilegal** dan **tidak etis**.

---

## 📘 Deskripsi

Ini adalah skrip **simulasi brute force** untuk mendemonstrasikan konsep percobaan login pada **MikroTik RouterOS melalui protokol Winbox berbasis MAC address**.

> ⚠️ Skrip ini **tidak benar-benar melakukan otentikasi** karena protokol Winbox MAC menggunakan **challenge-response terenkripsi**.

Tujuannya adalah untuk membantu pembelajaran mengenai:

- Konsep brute force dan mitigasinya
- Pengamanan Router MikroTik
- Pembuatan paket jaringan dengan Python + Scapy
- Etika dalam keamanan siber

---

## ⚙️ Kebutuhan Sistem

- OS Linux (Ubuntu, Kali, dsb.)
- Python 3.x
- Library Python: `scapy`

Instalasi:

```bash
pip install scapy

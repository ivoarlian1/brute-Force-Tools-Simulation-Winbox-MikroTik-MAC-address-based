# brute-Force-Tools-Simulation-Winbox-MikroTik-MAC-address-based

⚠️ Disclaimer Dulu:
Alat ini hanya boleh digunakan untuk:

Perangkat milik Anda sendiri

Lingkungan lab pribadi

Tujuan edukasi & pembelajaran keamanan jaringan

Menggunakan alat ini pada jaringan orang lain tanpa izin adalah ilegal dan melanggar etika profesional IT.

🎯 Tujuan Simulasi:
Melakukan brute force login terhadap Router MikroTik via MAC Winbox protocol (Port 20561), yang menggunakan MAC telnet-like protocol (Layer 2) — bukan berbasis IP.

📦 Persiapan:
🔧 Alat yang Dibutuhkan:
OS: Linux (Ubuntu/Kali)

Python 3

scapy (library untuk network packet crafting)

MikroTik router dalam mode lab

🧠 Penjelasan:
Protokol MAC Winbox bersifat proprietary dan menggunakan enkripsi (AES/RC4).

Anda tidak bisa langsung brute force dengan kirim string login+password — Anda harus handle handshake, challenge-response, dan enkripsi.

Mikrotik menutup dokumentasi protokol ini, jadi brute force hanya bisa dilakukan jika Anda reverse engineer protokolnya (seperti yang dilakukan oleh tool winboxexploit.py saat CVE lama ditemukan).

🔒 Rekomendasi Legal & Etis:
Gunakan alat open-source seperti RouterOS-Toolbox (untuk audit).

Gunakan log MikroTik + firewall rule untuk mendeteksi percobaan brute force.

📚 Referensi Legal:
RouterOS Brute Forcing dengan Python (forum edukatif)

PCAP Winbox Analysis (Wireshark capture)

MikroTik Challenge Auth Explanation

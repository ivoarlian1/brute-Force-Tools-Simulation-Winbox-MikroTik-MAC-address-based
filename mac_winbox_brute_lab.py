from scapy.all import *
import binascii
import time

# MAC address MikroTik Router (pastikan dari lab Anda sendiri)
target_mac = "6C:3B:6B:12:34:56"
interface = "eth0"  # ubah ke interface yang mengarah ke router

# Username yang akan dicoba
username = "admin"

# List password untuk dicoba
passwords = ["admin", "123456", "toor", "mikrotik", "labonly"]

def make_winbox_packet(mac_dst, username, password):
    """
    Ini adalah fungsi dummy. Protokol Winbox MAC sebenarnya kompleks
    dan menggunakan enkripsi challenge-response, jadi tidak bisa brute force
    pakai string biasa saja.
    Untuk edukasi, kita hanya bisa simulasi.
    """
    print(f"[*] Trying password: {password}")
    # Di sini seharusnya ada crafting untuk packet dengan format winbox
    # Tapi karena protokolnya proprietary & terenkripsi, ini hanya simulasi
    return None

def simulate_brute_force():
    for password in passwords:
        pkt = make_winbox_packet(target_mac, username, password)
        if pkt:
            sendp(pkt, iface=interface, verbose=False)
        time.sleep(1)

simulate_brute_force()

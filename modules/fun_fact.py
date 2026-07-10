#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from config import Colors, clear_screen

FACTS = [
    "🌐 Internet pertama kali disebut 'Information Superhighway'.",
    "💻 Bug komputer pertama adalah ngengat sungguhan yang ditemukan di relay Harvard Mark II tahun 1947.",
    "🔐 Password paling umum di dunia adalah '123456'.",
    "📱 Ada lebih banyak perangkat mobile daripada jumlah penduduk dunia.",
    "🤖 AI pertama kali diciptakan sebagai konsep pada tahun 1956 di Dartmouth Conference.",
    "🖥️ Bahasa pemrograman Python dinamai dari Monty Python, bukan ular.",
    "🌍 Setiap hari, 500 juta tweet dikirim di Twitter.",
    "📧 Email pertama dikirim oleh Ray Tomlinson tahun 1971.",
    "🔍 Google memproses lebih dari 8.5 miliar pencarian per hari.",
    "🎮 Video game pertama adalah 'Tennis for Two' dibuat tahun 1958.",
    "💾 Floppy disk pertama hanya bisa menyimpan 80KB data.",
    "⌨️ Keyboard QWERTY dirancang untuk memperlambat pengetikan agar mesin tik tidak macet.",
    "🦠 Virus komputer pertama bernama 'Creeper' dibuat tahun 1971.",
    "📡 WiFi pertama kali diperkenalkan tahun 1997 dengan kecepatan 2Mbps.",
    "🔒 HTTPS ditemukan oleh Netscape tahun 1994.",
    "💡 Thomas Edison tidak menemukan bola lampu, dia hanya menyempurnakannya.",
    "🚀 NASA menggunakan kode 1960-an untuk roket modern karena sudah terbukti handal.",
    "🎵 MP3 ditemukan oleh tim Fraunhofer Jerman tahun 1993.",
    "📸 Foto digital pertama diambil tahun 1957 — 20 tahun sebelum kamera digital.",
    "⚡ ALGORITMAZXXX v6.1 adalah tools cyber paling keren!",
]

def run():
    """Random Fact Generator"""
    clear_screen()
    print(f"{Colors.YELLOW}")
    print("╔════════════════════════════════════════╗")
    print("║        🧠 RANDOM FACT GENERATOR         ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    fact = random.choice(FACTS)
    
    print(f"\n{Colors.GREEN}")
    print(f"  ╔══════════════════════════════════════════╗")
    print(f"  ║  🧠 DID YOU KNOW?                        ║")
    print(f"  ║                                          ║")
    print(f"  ║  {fact}")
    print(f"  ║                                          ║")
    print(f"  ╚══════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    another = input(f"\n{Colors.YELLOW}🎲 Generate another? (y/n): {Colors.RESET}")
    if another.lower() == 'y':
        run()

if __name__ == "__main__":
    run()

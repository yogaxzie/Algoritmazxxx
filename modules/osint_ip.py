#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from config import Colors, clear_screen

def run():
    """IP Geolocation using ip-api.com"""
    clear_screen()
    print(f"{Colors.YELLOW}")
    print("╔════════════════════════════════════════╗")
    print("║        🌐 IP GEOLOCATION TOOL           ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    ip = input(f"\n{Colors.CYAN}🌐 Masukkan IP (kosongkan untuk IP sendiri): {Colors.RESET}")
    
    print(f"\n{Colors.YELLOW}🔍 Mencari lokasi IP...{Colors.RESET}")
    
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('status') == 'success':
            print(f"\n{Colors.GREEN}╔════════════════════════════════════════╗")
            print(f"║        🌐 IP GEOLOCATION RESULT         ║")
            print(f"╠════════════════════════════════════════╣")
            print(f"║  📡 IP         : {data.get('query')}")
            print(f"║  🌍 Negara     : {data.get('country')}")
            print(f"║  🏙️  Kota       : {data.get('city')}")
            print(f"║  📍 Region     : {data.get('regionName')}")
            print(f"║  📮 Kode Pos   : {data.get('zip')}")
            print(f"║  🕐 Timezone   : {data.get('timezone')}")
            print(f"║  📡 ISP        : {data.get('isp')}")
            print(f"║  🏢 Org        : {data.get('org')}")
            print(f"║  🗺️  Koordinat  : {data.get('lat')}, {data.get('lon')}")
            print(f"╚════════════════════════════════════════╝")
            print(f"\n{Colors.GREEN}✅ Lokasi berhasil ditemukan!")
        else:
            print(f"\n{Colors.RED}❌ IP tidak valid atau private!{Colors.RESET}")
            
    except requests.ConnectionError:
        print(f"\n{Colors.RED}❌ Tidak ada koneksi internet!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {e}{Colors.RESET}")

if __name__ == "__main__":
    run()

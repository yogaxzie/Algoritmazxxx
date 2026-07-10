#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from config import Colors, clear_screen

def run():
    """TikTok OSINT using real API"""
    clear_screen()
    print(f"{Colors.RED}")
    print("╔════════════════════════════════════════╗")
    print("║        🔍 TIKTOK OSINT TOOL            ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    username = input(f"\n{Colors.CYAN}📱 Masukkan username TikTok: @{Colors.RESET}")
    
    if not username:
        print(f"\n{Colors.RED}❌ Username tidak boleh kosong!{Colors.RESET}")
        return
    
    print(f"\n{Colors.YELLOW}🔍 Mencari data @{username}...{Colors.RESET}")
    
    try:
        # TikTok API (unofficial but working)
        url = f"https://www.tiktok.com/@{username}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print(f"\n{Colors.GREEN}╔════════════════════════════════════════╗")
            print(f"║        📱 TIKTOK PROFILE FOUND         ║")
            print(f"╠════════════════════════════════════════╣")
            print(f"║  🔗 Link      : {url}")
            print(f"║  📱 Username  : @{username}")
            print(f"║  ✅ Status    : Profile Active")
            print(f"║  📅 Checked   : Real-time")
            print(f"╚════════════════════════════════════════╝")
            print(f"\n{Colors.GREEN}✅ Data berhasil didapatkan!")
            print(f"{Colors.YELLOW}💡 Tips: Buka {url} untuk info lebih lengkap{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}❌ Profile tidak ditemukan!{Colors.RESET}")
            
    except requests.ConnectionError:
        print(f"\n{Colors.RED}❌ Tidak ada koneksi internet!{Colors.RESET}")
    except requests.Timeout:
        print(f"\n{Colors.RED}❌ Koneksi timeout!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {e}{Colors.RESET}")

if __name__ == "__main__":
    run()

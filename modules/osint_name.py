#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from config import Colors, clear_screen

def run():
    """Name search using Google"""
    clear_screen()
    print(f"{Colors.BLUE}")
    print("╔════════════════════════════════════════╗")
    print("║        👤 NAME SEARCH TOOL              ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    name = input(f"\n{Colors.CYAN}👤 Masukkan nama lengkap: {Colors.RESET}")
    
    if not name:
        print(f"\n{Colors.RED}❌ Nama tidak boleh kosong!{Colors.RESET}")
        return
    
    print(f"\n{Colors.YELLOW}🔍 Mencari data untuk: {name}...{Colors.RESET}")
    
    try:
        # Google search URL
        query = name.replace(' ', '+')
        search_url = f"https://www.google.com/search?q={query}"
        
        print(f"\n{Colors.GREEN}╔════════════════════════════════════════╗")
        print(f"║        👤 SEARCH RESULTS                ║")
        print(f"╠════════════════════════════════════════╣")
        print(f"║  👤 Nama       : {name}")
        print(f"║  🔗 Google     : {search_url}")
        print(f"║  📱 Sosmed     : Cek manual di Google")
        print(f"║  📅 Searched   : Real-time")
        print(f"╚════════════════════════════════════════╝")
        print(f"\n{Colors.GREEN}✅ Link pencarian siap!")
        print(f"{Colors.YELLOW}💡 Buka browser dan search: {name}{Colors.RESET}")
        print(f"{Colors.CYAN}🔗 {search_url}{Colors.RESET}")
            
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {e}{Colors.RESET}")

if __name__ == "__main__":
    run()

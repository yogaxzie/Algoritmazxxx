#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from config import *
from modules import (
    osint_tiktok, osint_instagram, osint_whatsapp,
    osint_name, osint_ip, hacking_scan,
    tools_hash, tools_password, tools_encrypt,
    fun_quote, fun_fact, system_info
)

class AlgoritmazxxxTermux:
    def __init__(self):
        self.attempts = 0
        self.authenticated = False
    
    def pin_login(self):
        """PIN login screen"""
        clear_screen()
        print(BANNER)
        print(f"""
{Fore.YELLOW}┌──────────────────────────────────────────────────────────┐
│  🟢 SYSTEM BOOT SUCCESSFUL                               │
│  👤 USER    : root@algoritmazxxx                         │
│  💰 BALANCE : {SYSTEM_CONFIG['saldo']}                    
│  🔐 STATUS  : LOCKED — PIN REQUIRED                      │
└──────────────────────────────────────────────────────────┘{Fore.RESET}
""")
        
        while self.attempts < SYSTEM_CONFIG['max_attempts']:
            pin = input(f"\n{Fore.CYAN}🔐 MASUKKAN PIN AKSES: {Fore.RESET}")
            
            if verify_pin(pin):
                self.authenticated = True
                print(f"\n{Fore.GREEN}✅ ACCESS GRANTED — SELAMAT DATANG, DEVELOPER!{Fore.RESET}")
                print(f"{Fore.RED}🔥 ALGORITMAZXXX TERMUX v{SYSTEM_CONFIG['version']} AKTIF{Fore.RESET}")
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Fore.RESET}")
                return True
            else:
                self.attempts += 1
                remaining = SYSTEM_CONFIG['max_attempts'] - self.attempts
                print(f"\n{Fore.RED}❌ ACCESS DENIED — PIN SALAH!{Fore.RESET}")
                print(f"{Fore.YELLOW}⚠️  SISA PERCOBAAN: {remaining}{Fore.RESET}")
                
                if self.attempts >= SYSTEM_CONFIG['max_attempts']:
                    print(f"\n{Fore.RED}🚨 3x SALAH — SYSTEM LOCKED PERMANENT!{Fore.RESET}")
                    sys.exit(1)
        
        return False
    
    def show_main_menu(self):
        """Show main menu"""
        clear_screen()
        print(BANNER)
        print(f"""
{Fore.GREEN}✅ AUTHENTICATED — root@algoritmazxxx{Fore.RESET}
{Fore.RED}💰 SALDO: {SYSTEM_CONFIG['saldo']}{Fore.RESET}

{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                        📋 MAIN MENU                          ║
╠══════════════════════════════════════════════════════════════╣
║  [01] 🔍 TikTok OSINT        [02] 📸 Instagram OSINT        ║
║  [03] 📱 WhatsApp OSINT      [04] 👤 Name Search            ║
║  [05] 🌐 IP Geolocation      [06] 🔍 Port Scanner           ║
║  [07] 🔐 Hash Tools          [08] 🔑 Password Generator     ║
║  [09] 🔒 File Encrypt/Decrypt[10] 💻 System Info            ║
║  [11] 💬 Random Quote        [12] 🧠 Random Fact            ║
║                                                              ║
║  [99] 🔒 LOCK SYSTEM         [00] 🚪 EXIT                   ║
╚══════════════════════════════════════════════════════════════╝{Fore.RESET}
""")
    
    def run_tool(self, choice):
        """Run selected tool"""
        tools = {
            '1': osint_tiktok.run,
            '2': osint_instagram.run,
            '3': osint_whatsapp.run,
            '4': osint_name.run,
            '5': osint_ip.run,
            '6': hacking_scan.run,
            '7': tools_hash.run,
            '8': tools_password.run,
            '9': tools_encrypt.run,
            '10': system_info.run,
            '11': fun_quote.run,
            '12': fun_fact.run,
        }
        
        if choice in tools:
            tools[choice]()
            input(f"\n{Fore.YELLOW}Press Enter to return to menu...{Fore.RESET}")
        elif choice == '99':
            print(f"\n{Fore.RED}🔒 SYSTEM LOCKED{Fore.RESET}")
            self.authenticated = False
            self.attempts = 0
            self.run()
        elif choice == '00':
            print(f"\n{Fore.GREEN}👋 Goodbye, Developer!{Fore.RESET}")
            sys.exit(0)
        else:
            print(f"\n{Fore.RED}❌ Invalid choice!{Fore.RESET}")
            input(f"{Fore.YELLOW}Press Enter to continue...{Fore.RESET}")
    
    def run(self):
        """Main run loop"""
        if not self.authenticated:
            if not self.pin_login():
                return
        
        while True:
            self.show_main_menu()
            choice = input(f"{Fore.GREEN}root@algoritmazxxx:~# {Fore.RESET}")
            self.run_tool(choice)

if __name__ == "__main__":
    app = AlgoritmazxxxTermux()
    app.run()

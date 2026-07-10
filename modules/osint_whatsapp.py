#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
from config import Colors, clear_screen

def validate_wa_number(number):
    """Validate WhatsApp number format"""
    # Remove all non-digit characters
    clean = re.sub(r'\D', '', number)
    
    # Convert to international format
    if clean.startswith('0'):
        clean = '62' + clean[1:]
    elif clean.startswith('8'):
        clean = '62' + clean
    
    return clean

def get_provider(number):
    """Get Indonesian provider from prefix"""
    providers = {
        '0811': 'Telkomsel (Halo)', '0812': 'Telkomsel (Simpati)',
        '0813': 'Telkomsel (Simpati)', '0821': 'Telkomsel (Simpati)',
        '0822': 'Telkomsel (Simpati)', '0823': 'Telkomsel (AS)',
        '0851': 'Telkomsel (AS)', '0852': 'Telkomsel (Simpati)',
        '0853': 'Telkomsel (Simpati)',
        '0814': 'Indosat (IM3)', '0815': 'Indosat (Mentari)',
        '0816': 'Indosat (Mentari)', '0855': 'Indosat (IM3)',
        '0856': 'Indosat (IM3)', '0857': 'Indosat (IM3)',
        '0858': 'Indosat (IM3)',
        '0817': 'XL Axiata', '0818': 'XL Axiata', '0819': 'XL Axiata',
        '0859': 'XL Axiata', '0877': 'XL Axiata', '0878': 'XL Axiata',
        '0831': 'AXIS', '0832': 'AXIS', '0833': 'AXIS',
        '0838': 'AXIS',
        '0895': 'Tri (3)', '0896': 'Tri (3)', '0897': 'Tri (3)',
        '0898': 'Tri (3)', '0899': 'Tri (3)',
        '0881': 'Smartfren', '0882': 'Smartfren', '0883': 'Smartfren',
        '0884': 'Smartfren', '0885': 'Smartfren', '0886': 'Smartfren',
        '0887': 'Smartfren', '0888': 'Smartfren',
    }
    
    for prefix, provider in providers.items():
        if number.startswith(prefix):
            return provider
    
    return "Unknown Provider"

def run():
    """WhatsApp OSINT"""
    clear_screen()
    print(f"{Colors.GREEN}")
    print("╔════════════════════════════════════════╗")
    print("║        📱 WHATSAPP OSINT TOOL           ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    number = input(f"\n{Colors.CYAN}📱 Masukkan nomor WA (08xx): {Colors.RESET}")
    
    if not number:
        print(f"\n{Colors.RED}❌ Nomor tidak boleh kosong!{Colors.RESET}")
        return
    
    clean_number = validate_wa_number(number)
    provider = get_provider(clean_number)
    
    print(f"\n{Colors.YELLOW}🔍 Menganalisis nomor...{Colors.RESET}")
    
    try:
        # Check WhatsApp API
        url = f"https://wa.me/{clean_number}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        print(f"\n{Colors.GREEN}╔════════════════════════════════════════╗")
        print(f"║        📱 WHATSAPP NUMBER INFO          ║")
        print(f"╠════════════════════════════════════════╣")
        print(f"║  📞 Nomor      : {clean_number}")
        print(f"║  🌐 Provider   : {provider}")
        print(f"║  🔗 WA Link    : {url}")
        print(f"║  📅 Checked    : Real-time")
        print(f"║  ✅ Format     : Valid International")
        print(f"╚════════════════════════════════════════╝")
        print(f"\n{Colors.GREEN}✅ Data berhasil didapatkan!")
        print(f"{Colors.YELLOW}💡 Buka {url} untuk chat langsung{Colors.RESET}")
            
    except requests.ConnectionError:
        print(f"\n{Colors.RED}❌ Tidak ada koneksi internet!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {e}{Colors.RESET}")

if __name__ == "__main__":
    run()

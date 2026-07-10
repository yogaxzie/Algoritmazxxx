#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
from config import Colors, clear_screen

def generate_hash(text, algo):
    """Generate hash"""
    algorithms = {
        '1': ('MD5', hashlib.md5),
        '2': ('SHA1', hashlib.sha1),
        '3': ('SHA256', hashlib.sha256),
        '4': ('SHA512', hashlib.sha512),
        '5': ('BLAKE2b', hashlib.blake2b),
        '6': ('BLAKE2s', hashlib.blake2s),
    }
    
    if algo in algorithms:
        name, func = algorithms[algo]
        if algo in ['5', '6']:
            hash_result = func(text.encode()).hexdigest()
        else:
            hash_result = func(text.encode()).hexdigest()
        return name, hash_result
    return None, None

def run():
    """Hash Generator"""
    clear_screen()
    print(f"{Colors.CYAN}")
    print("╔════════════════════════════════════════╗")
    print("║        🔐 HASH GENERATOR TOOL           ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    text = input(f"\n{Colors.CYAN}📝 Masukkan text: {Colors.RESET}")
    
    if not text:
        print(f"\n{Colors.RED}❌ Text tidak boleh kosong!{Colors.RESET}")
        return
    
    print(f"\n{Colors.YELLOW}Pilih algoritma:")
    print(f"  [1] MD5")
    print(f"  [2] SHA1")
    print(f"  [3] SHA256")
    print(f"  [4] SHA512")
    print(f"  [5] BLAKE2b")
    print(f"  [6] BLAKE2s{Colors.RESET}")
    
    choice = input(f"\n{Colors.CYAN}Pilih [1-6]: {Colors.RESET}")
    
    name, result = generate_hash(text, choice)
    
    if name and result:
        print(f"\n{Colors.GREEN}╔════════════════════════════════════════╗")
        print(f"║        🔐 HASH RESULT                   ║")
        print(f"╠════════════════════════════════════════╣")
        print(f"║  📝 Input      : {text[:50]}{'...' if len(text) > 50 else ''}")
        print(f"║  🔧 Algorithm  : {name}")
        print(f"║  🔐 Hash       : {result}")
        print(f"╚════════════════════════════════════════╝")
        print(f"\n{Colors.GREEN}✅ Hash berhasil dibuat!{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}❌ Pilihan tidak valid!{Colors.RESET}")

if __name__ == "__main__":
    run()

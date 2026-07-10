#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from cryptography.fernet import Fernet
from config import Colors, clear_screen

def generate_key():
    """Generate encryption key"""
    return Fernet.generate_key()

def encrypt_file(filename, key):
    """Encrypt a file"""
    fernet = Fernet(key)
    
    with open(filename, 'rb') as f:
        data = f.read()
    
    encrypted = fernet.encrypt(data)
    
    with open(filename + '.encrypted', 'wb') as f:
        f.write(encrypted)
    
    return True

def decrypt_file(filename, key):
    """Decrypt a file"""
    fernet = Fernet(key)
    
    with open(filename, 'rb') as f:
        data = f.read()
    
    decrypted = fernet.decrypt(data)
    
    output_name = filename.replace('.encrypted', '.decrypted')
    with open(output_name, 'wb') as f:
        f.write(decrypted)
    
    return True

def run():
    """File Encrypt/Decrypt Tool"""
    clear_screen()
    print(f"{Colors.RED}")
    print("╔════════════════════════════════════════╗")
    print("║        🔒 FILE ENCRYPT/DECRYPT          ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    print(f"\n{Colors.CYAN}Pilih operasi:")
    print(f"  [1] 🔒 Encrypt File")
    print(f"  [2] 🔓 Decrypt File")
    print(f"  [3] 🔑 Generate Key{Colors.RESET}")
    
    choice = input(f"\n{Colors.CYAN}Pilih [1-3]: {Colors.RESET}")
    
    if choice == '3':
        key = generate_key()
        print(f"\n{Colors.GREEN}╔════════════════════════════════════════╗")
        print(f"║        🔑 GENERATED KEY                 ║")
        print(f"╠════════════════════════════════════════╣")
        print(f"║  🔑 Key: {key.decode()}")
        print(f"╚════════════════════════════════════════╝")
        print(f"\n{Colors.YELLOW}⚠️  SIMPAN KEY INI! Tanpa key, file tidak bisa didekripsi!{Colors.RESET}")
        return
    
    if choice in ['1', '2']:
        filename = input(f"\n{Colors.CYAN}📁 Nama file: {Colors.RESET}")
        
        if not os.path.exists(filename):
            print(f"\n{Colors.RED}❌ File tidak ditemukan!{Colors.RESET}")
            return
        
        key_input = input(f"{Colors.CYAN}🔑 Masukkan key: {Colors.RESET}")
        
        try:
            key = key_input.encode()
            
            if choice == '1':
                if encrypt_file(filename, key):
                    print(f"\n{Colors.GREEN}✅ File berhasil dienkripsi!")
                    print(f"📁 Output: {filename}.encrypted{Colors.RESET}")
            else:
                if decrypt_file(filename, key):
                    print(f"\n{Colors.GREEN}✅ File berhasil didekripsi!")
                    print(f"📁 Output: {filename.replace('.encrypted', '.decrypted')}{Colors.RESET}")
                    
        except Exception as e:
            print(f"\n{Colors.RED}❌ Error: Key salah atau file corrupt!{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}❌ Pilihan tidak valid!{Colors.RESET}")

if __name__ == "__main__":
    run()

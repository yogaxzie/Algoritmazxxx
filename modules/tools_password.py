#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
from config import Colors, clear_screen

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate random password"""
    chars = ''
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    if not chars:
        return None
    
    password = ''.join(random.choice(chars) for _ in range(length))
    
    # Check strength
    strength = "WEAK"
    if length >= 12 and use_upper and use_lower and use_digits and use_symbols:
        strength = "VERY STRONG"
    elif length >= 10 and ((use_upper and use_lower and use_digits) or (use_upper and use_lower and use_symbols)):
        strength = "STRONG"
    elif length >= 8:
        strength = "MEDIUM"
    
    return password, strength

def run():
    """Password Generator"""
    clear_screen()
    print(f"{Colors.MAGENTA}")
    print("╔════════════════════════════════════════╗")
    print("║        🔑 PASSWORD GENERATOR            ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    try:
        length = int(input(f"\n{Colors.CYAN}📏 Panjang password (min 8): {Colors.RESET}"))
        if length < 8:
            length = 8
            print(f"{Colors.YELLOW}⚠️  Minimal 8 karakter, diset ke 8{Colors.RESET}")
    except:
        length = 12
        print(f"{Colors.YELLOW}⚠️  Input invalid, diset ke 12{Colors.RESET}")
    
    print(f"\n{Colors.YELLOW}Pilih karakter yang digunakan:{Colors.RESET}")
    use_upper = input(f"  Huruf besar? (y/n): ").lower() == 'y'
    use_lower = input(f"  Huruf kecil? (y/n): ").lower() == 'y'
    use_digits = input(f"  Angka? (y/n): ").lower() == 'y'
    use_symbols = input(f"  Simbol? (y/n): ").lower() == 'y'
    
    print(f"\n{Colors.YELLOW}🔑 Generating password...{Colors.RESET}")
    
    password, strength = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    
    if password:
        strength_color = {
            'VERY STRONG': Colors.GREEN,
            'STRONG': Colors.GREEN,
            'MEDIUM': Colors.YELLOW,
            'WEAK': Colors.RED
        }.get(strength, Colors.RED)
        
        print(f"\n{Colors.GREEN}╔════════════════════════════════════════╗")
        print(f"║        🔑 GENERATED PASSWORD            ║")
        print(f"╠════════════════════════════════════════╣")
        print(f"║  🔑 Password   : {password}")
        print(f"║  📏 Length     : {len(password)} chars")
        print(f"║  💪 Strength   : {strength_color}{strength}{Colors.GREEN}")
        print(f"╚════════════════════════════════════════╝")
        print(f"\n{Colors.GREEN}✅ Password berhasil dibuat!")
        print(f"{Colors.YELLOW}💡 Simpan password ini di tempat aman!{Colors.RESET}")
    else:
        print(f"\n{Colors.RED}❌ Pilih minimal 1 jenis karakter!{Colors.RESET}")

if __name__ == "__main__":
    run()

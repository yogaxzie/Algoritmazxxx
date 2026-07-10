#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform
import socket
from datetime import datetime
from config import Colors, clear_screen, SYSTEM_CONFIG

def get_size(bytes_val):
    """Convert bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024
    return f"{bytes_val:.2f} PB"

def run():
    """System Information"""
    clear_screen()
    print(f"{Colors.CYAN}")
    print("╔════════════════════════════════════════╗")
    print("║        💻 SYSTEM INFORMATION            ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    except:
        hostname = "Unknown"
        ip = "Unknown"
    
    print(f"\n{Colors.GREEN}╔════════════════════════════════════════╗")
    print(f"║        🖥️  SYSTEM INFO                   ║")
    print(f"╠════════════════════════════════════════╣")
    print(f"║  🤖 System     : {SYSTEM_CONFIG['name']} v{SYSTEM_CONFIG['version']}")
    print(f"║  💻 OS         : {platform.system()} {platform.release()}")
    print(f"║  🏗️  Arch       : {platform.machine()}")
    print(f"║  🐍 Python     : {platform.python_version()}")
    print(f"║  👤 Hostname   : {hostname}")
    print(f"║  📡 IP Local   : {ip}")
    print(f"║  📅 Date       : {datetime.now().strftime('%d %B %Y')}")
    print(f"║  🕐 Time       : {datetime.now().strftime('%H:%M:%S WIB')}")
    print(f"║  💰 Balance    : {SYSTEM_CONFIG['saldo']}")
    print(f"║  🔒 Security   : PINLOCK OMEGA")
    print(f"║  👤 User       : root@algoritmazxxx")
    print(f"╚════════════════════════════════════════╝")
    print(f"\n{Colors.GREEN}✅ System info retrieved successfully!{Colors.RESET}")

if __name__ == "__main__":
    run()

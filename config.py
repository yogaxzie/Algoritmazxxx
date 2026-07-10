#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# System Configuration
SYSTEM_CONFIG = {
    "name": "ALGORITMAZXXX",
    "version": "6.1",
    "edition": "TERMUX PINLOCK OMEGA",
    "developer": "7779-mailaka yastra",
    "pin": "algoritmazxxx",
    "saldo": "$999.999.999.999.999.999,00",
    "max_attempts": 3
}

# Colors
class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
    BRIGHT = Style.BRIGHT

# Banner
BANNER = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════╗
║  █████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗████████╗██╗  ██╗███████╗
║  ██╔══██╗██║     ██╔════╝ ██╔═══██╗██╔══██╗██║╚══██╔══╝██║  ██║██╔════╝
║  ███████║██║     ██║  ███╗██║   ██║██████╔╝██║   ██║   ███████║█████╗  
║  ██╔══██║██║     ██║   ██║██║   ██║██╔══██╗██║   ██║   ██╔══██║██╔══╝  
║  ██║  ██║███████╗╚██████╔╝╚██████╔╝██║  ██║██║   ██║   ██║  ██║███████╗
║  ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
║  
║  ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
║  ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝
║     ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝ 
║     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗ 
║     ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
║     ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
║                                                              
║     🔥 v{SYSTEM_CONFIG['version']} {SYSTEM_CONFIG['edition']} 🔥
║     💀 CYBREXO-GRADIVALZZZAI — REAL TOOLS 💀
╚══════════════════════════════════════════════════════════════╝{Fore.RESET}
"""

def verify_pin(pin_input):
    """Verify PIN"""
    return pin_input == SYSTEM_CONFIG["pin"]

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

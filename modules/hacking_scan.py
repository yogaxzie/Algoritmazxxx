#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
from datetime import datetime
from config import Colors, clear_screen

def scan_port(host, port):
    """Scan single port"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

def get_service(port):
    """Get common service name"""
    services = {
        21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
        53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP',
        443: 'HTTPS', 3306: 'MySQL', 3389: 'RDP', 8080: 'HTTP-Proxy',
        8443: 'HTTPS-Alt', 9090: 'Webmin'
    }
    return services.get(port, 'Unknown')

def run():
    """Port Scanner"""
    clear_screen()
    print(f"{Colors.RED}")
    print("╔════════════════════════════════════════╗")
    print("║        🔍 PORT SCANNER TOOL             ║")
    print("║        ⚠️ ONLY SCAN OWN DEVICES!        ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    host = input(f"\n{Colors.CYAN}🎯 Target IP/Host: {Colors.RESET}")
    
    if not host:
        print(f"\n{Colors.RED}❌ Target tidak boleh kosong!{Colors.RESET}")
        return
    
    print(f"\n{Colors.YELLOW}🔍 Scanning {host}...{Colors.RESET}")
    print(f"{Colors.YELLOW}⏱️  Started at: {datetime.now().strftime('%H:%M:%S')}{Colors.RESET}\n")
    
    start_time = datetime.now()
    open_ports = []
    
    # Common ports to scan
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080, 8443, 9090]
    
    for port in ports:
        try:
            if scan_port(host, port):
                service = get_service(port)
                open_ports.append((port, service))
                print(f"{Colors.GREEN}  ✅ Port {port} OPEN — {service}{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}❌ Scan dihentikan!{Colors.RESET}")
            return
        except:
            pass
    
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print(f"\n{Colors.CYAN}╔════════════════════════════════════════╗")
    print(f"║        📊 SCAN RESULT                   ║")
    print(f"╠════════════════════════════════════════╣")
    print(f"║  🎯 Target     : {host}")
    print(f"║  🔓 Open Ports : {len(open_ports)}")
    print(f"║  ⏱️  Duration   : {duration:.2f}s")
    print(f"╚════════════════════════════════════════╝")
    print(f"\n{Colors.GREEN}✅ Scan selesai!{Colors.RESET}")
    print(f"{Colors.YELLOW}⚠️  HANYA GUNAKAN UNTUK DEVICE SENDIRI!{Colors.RESET}")

if __name__ == "__main__":
    run()

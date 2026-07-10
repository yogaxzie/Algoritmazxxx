#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from config import Colors, clear_screen

QUOTES = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Stay hungry, stay foolish.", "Steve Jobs"),
    ("Think different.", "Apple Inc."),
    ("Innovation distinguishes between a leader and a follower.", "Steve Jobs"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("Experience is the name everyone gives to their mistakes.", "Oscar Wilde"),
    ("The best way to predict the future is to create it.", "Peter Drucker"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("Knowledge is power.", "Francis Bacon"),
    ("The only impossible journey is the one you never begin.", "Tony Robbins"),
    ("Security is not a product, but a process.", "Bruce Schneier"),
    ("Hack the planet!", "Hackers Movie"),
    ("There is no cloud, it's just someone else's computer.", "Unknown"),
    ("It's not a bug — it's an undocumented feature.", "Unknown"),
    ("I have not failed. I've just found 10,000 ways that won't work.", "Thomas Edison"),
    ("The quieter you become, the more you can hear.", "Unknown"),
    ("In a world of algorithms, be the exception.", "ALGORITMAZXXX"),
]

def run():
    """Random Quote Generator"""
    clear_screen()
    print(f"{Colors.MAGENTA}")
    print("╔════════════════════════════════════════╗")
    print("║        💬 RANDOM QUOTE GENERATOR        ║")
    print("╚════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    quote, author = random.choice(QUOTES)
    
    print(f"\n{Colors.CYAN}")
    print(f"  ╔══════════════════════════════════════════╗")
    print(f"  ║  💬 QUOTE OF THE DAY:                    ║")
    print(f"  ║                                          ║")
    print(f"  ║  \"{quote}\"")
    print(f"  ║                                          ║")
    print(f"  ║  — {author}")
    print(f"  ╚══════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
    another = input(f"\n{Colors.YELLOW}🎲 Generate another? (y/n): {Colors.RESET}")
    if another.lower() == 'y':
        run()

if __name__ == "__main__":
    run()

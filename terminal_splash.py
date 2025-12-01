#!/usr/bin/env python3
"""
Terminal Splash Screen - Professional Hacker Edition
A sleek, cyberpunk-themed welcome screen for your terminal
"""

import os
import sys
import platform
import subprocess
import json
import requests
import random
from datetime import datetime
from pathlib import Path

class Colors:
    """ANSI color codes for cyberpunk theme"""
    # Purple/Magenta spectrum (main theme)
    PURPLE = '\033[95m'
    MAGENTA = '\033[35m'
    BRIGHT_PURPLE = '\033[1;35m'
    
    # Cyan/Blue (accent colors)
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    BRIGHT_CYAN = '\033[1;36m'
    
    # Green (success/online)
    GREEN = '\033[92m'
    BRIGHT_GREEN = '\033[1;32m'
    
    # Other colors
    RED = '\033[91m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class TerminalSplash:
    def __init__(self):
        self.config = self.load_config()
        self.width = self.get_terminal_width()
        
    def load_config(self):
        """Load configuration from file or create defaults"""
        config_path = Path.home() / '.config' / 'terminal_splash' / 'config.json'
        default_config = {
            'show_quotes': True,
            'show_system_info': True,
            'ask_update': True,
            'ascii_style': 'cyberpunk'
        }
        
        # Create config directory if it doesn't exist
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    user_config = json.load(f)
                default_config.update(user_config)
            except Exception as e:
                pass
        else:
            # Save default config
            try:
                with open(config_path, 'w') as f:
                    json.dump(default_config, f, indent=4)
            except:
                pass
        
        return default_config
    
    def get_terminal_width(self):
        """Get terminal width for proper formatting"""
        try:
            return os.get_terminal_size().columns
        except:
            return 80
    
    def get_ascii_art(self):
        """Professional ASCII art - Anonymous hacker mask"""
        art = [
            f"{Colors.PURPLE}⠀⢠⣶⣿⣿⣗⡢⠀⠀⠀⠀⠀⠀⢤⣒⣿⣿⣷⣆⠀⠀",
            f"{Colors.PURPLE}⠀⠋⠉⠉⠙⠻⣿⣷⡄⠀⠀⠀⣴⣿⠿⠛⠉⠉⠉⠃⠀",
            f"{Colors.CYAN}⠀⠀⢀⡠⢤⣠⣀⡹⡄⠀⠀⠀⡞⣁⣤⣠⠤⡀⠀⠀⠀",
            f"{Colors.CYAN}⢐⡤⢾⣿⣿⢿⣿⡿⠀⠀⠀⠀⠸⣿⣿⢿⣿⣾⠦⣌⠀",
            f"{Colors.CYAN}⠁⠀⠀⠀⠉⠈⠀⠀⣸⠀⠀⢰⡀⠀⠈⠈⠀⠀⠀⠀⠁",
            f"{Colors.BRIGHT_CYAN}⠀⠀⠀⠀⠀⠀⣀⡔⢹⠀⠀⢸⠳⡄⡀⠀⠀⠀⠀⠀⠀",
            f"{Colors.BRIGHT_CYAN}⠸⡦⣤⠤⠒⠋⠘⢠⡸⣀⣀⡸⣠⠘⠉⠓⠠⣤⢤⡞⠀",
            f"{Colors.BRIGHT_CYAN}⠀⢹⡜⢷⣄⠀⣀⣀⣾⡶⢶⣷⣄⣀⡀⢀⣴⢏⡾⠁⠀",
            f"{Colors.DIM}⠀⠀⠹⡮⡛⠛⠛⠻⠿⠥⠤⠽⠿⠛⠛⠛⣣⡾⠁⠀⠀",
            f"{Colors.DIM}⠀⠀⠀⠙⢄⠁⠀⠀⠀⣄⣀⡄⠀⠀⠀⢁⠞⠀⠀⠀⠀",
            f"{Colors.DIM}⠀⠀⠀⠀⠀⠂⠀⠀⠀⢸⣿⠀⠀⠀⠠⠂⠀⠀⠀⠀⠀",
            f"{Colors.DIM}⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            f"{Colors.DIM}⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            f"{Colors.END}"
        ]
        return art
    
    def get_system_info(self):
        """Gather detailed system information"""
        info = {}
        
        # OS Information
        info['os'] = f"{platform.system()} {platform.release()}"
        
        # Username and hostname
        info['user'] = os.getenv('USER', 'Unknown')
        info['hostname'] = platform.node()
        
        # Uptime
        try:
            if platform.system() == 'Linux':
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.readline().split()[0])
                    hours = int(uptime_seconds // 3600)
                    minutes = int((uptime_seconds % 3600) // 60)
                    info['uptime'] = f"{hours}h {minutes}m"
            elif platform.system() == 'Darwin':
                boot_time = subprocess.check_output(['sysctl', '-n', 'kern.boottime']).decode()
                # Parse and calculate uptime
                info['uptime'] = 'Available'
            else:
                info['uptime'] = 'N/A'
        except:
            info['uptime'] = 'N/A'
        
        # Memory usage
        try:
            if platform.system() == 'Linux':
                with open('/proc/meminfo', 'r') as f:
                    meminfo = f.read()
                    total = int([line for line in meminfo.split('\n') if 'MemTotal' in line][0].split()[1])
                    available = int([line for line in meminfo.split('\n') if 'MemAvailable' in line][0].split()[1])
                    used = total - available
                    info['memory_used'] = used // 1024
                    info['memory_total'] = total // 1024
                    info['memory_percent'] = (used / total) * 100
            else:
                info['memory_used'] = 0
                info['memory_total'] = 0
                info['memory_percent'] = 0
        except:
            info['memory_used'] = 0
            info['memory_total'] = 0
            info['memory_percent'] = 0
        
        # CPU information
        try:
            if platform.system() == 'Linux':
                with open('/proc/cpuinfo', 'r') as f:
                    cpuinfo = f.read()
                    model = [line for line in cpuinfo.split('\n') if 'model name' in line]
                    if model:
                        info['cpu'] = model[0].split(':')[1].strip()
                    else:
                        info['cpu'] = 'Unknown CPU'
            else:
                info['cpu'] = platform.processor() or 'Unknown CPU'
        except:
            info['cpu'] = platform.processor() or 'Unknown CPU'
        
        # Kernel
        try:
            info['kernel'] = platform.release()
        except:
            info['kernel'] = 'N/A'
        
        # Shell
        info['shell'] = os.getenv('SHELL', 'Unknown').split('/')[-1]
        
        return info
    
    def get_quote(self):
        """Get a random hacker/tech inspirational quote"""
        if not self.config['show_quotes']:
            return None
            
        quotes = [
            "The only truly secure system is one that is powered off, cast in a block of concrete and sealed in a lead-lined room. - Gene Spafford",
            "Talk is cheap. Show me the code. - Linus Torvalds",
            "The best way to predict the future is to invent it. - Alan Kay",
            "Hackers are breaking systems for profit. Meanwhile, they're stealing our identity and selling our data. - Tim Cook",
            "Code is like humor. When you have to explain it, it's bad. - Cory House",
            "First, solve the problem. Then, write the code. - John Johnson",
            "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. - Martin Fowler",
            "The computer was born to solve problems that did not exist before. - Bill Gates",
            "To err is human, but to really foul things up you need a computer. - Paul Ehrlich",
            "It's hardware that makes a machine fast. It's software that makes a fast machine slow. - Craig Bruce",
            "Privacy is not an option, and it shouldn't be the price we accept for just getting on the Internet. - Gary Kovacs",
            "Cybersecurity is much more than a matter of IT. - Stephane Nappo"
        ]
        
        return random.choice(quotes)
    
    def center_text(self, text):
        """Center text based on terminal width"""
        # Remove ANSI codes for length calculation
        import re
        clean_text = re.sub(r'\033\[[0-9;]+m', '', text)
        padding = (self.width - len(clean_text)) // 2
        return ' ' * max(0, padding) + text
    
    def display(self):
        """Display the complete splash screen"""
        # Clear screen
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print()
        
        # Divider
        divider = f"{Colors.GRAY}{'─' * 80}{Colors.END}"
        print(self.center_text(divider))
        print()

        # Status line
        status = f"{Colors.BRIGHT_GREEN}[{Colors.BOLD}SYSTEM STATUS{Colors.END}{Colors.BRIGHT_GREEN}]{Colors.END} {Colors.GREEN}●{Colors.END} {Colors.BRIGHT_GREEN}ONLINE{Colors.END}"
        print(self.center_text(status))
        print()
        print()
        # ASCII Art and System Information - centered layout
        if self.config['show_system_info']:
            info = self.get_system_info()
            ascii_art = self.get_ascii_art()
            
            # Print ASCII art centered
            for line in ascii_art:
                print(self.center_text(line))
            
            print()
            sys_info_lines = [
                f"{Colors.PURPLE}{Colors.BRIGHT_PURPLE}[{Colors.BRIGHT_CYAN}SYSTEM INFORMATION{Colors.BRIGHT_PURPLE}]{Colors.END}",
                f"{Colors.GRAY}--------------------------------------------------{Colors.END}",
                f"{Colors.PURPLE}├──{Colors.BRIGHT_CYAN}[{Colors.WHITE}USER{Colors.BRIGHT_CYAN}]{Colors.END}            {Colors.GREEN}{info['user']}@{info['hostname']}{Colors.END}",
                f"{Colors.PURPLE}├──{Colors.BRIGHT_CYAN}[{Colors.WHITE}OS{Colors.BRIGHT_CYAN}]{Colors.END}              {Colors.WHITE}{info['os']}{Colors.END}",
                f"{Colors.PURPLE}├──{Colors.BRIGHT_CYAN}[{Colors.WHITE}KERNEL{Colors.BRIGHT_CYAN}]{Colors.END}                {Colors.WHITE}{info['kernel']}{Colors.END}",
                f"{Colors.PURPLE}├──{Colors.BRIGHT_CYAN}[{Colors.WHITE}SHELL{Colors.BRIGHT_CYAN}]{Colors.END}                           {Colors.WHITE}{info['shell']}{Colors.END}",
                f"{Colors.PURPLE}├──{Colors.BRIGHT_CYAN}[{Colors.WHITE}UPTIME{Colors.BRIGHT_CYAN}]{Colors.END}                        {Colors.WHITE}{info['uptime']}{Colors.END}",
                f"{Colors.PURPLE}├──{Colors.BRIGHT_CYAN}[{Colors.WHITE}MEMORY{Colors.BRIGHT_CYAN}]{Colors.END}      {Colors.WHITE}{info['memory_used']}MB / {info['memory_total']}MB {Colors.PURPLE}({info['memory_percent']:.1f}%){Colors.END}",
                f"{Colors.GRAY}----->{Colors.BRIGHT_CYAN}[{Colors.WHITE}CPU{Colors.BRIGHT_CYAN}]{Colors.END} {Colors.YELLOW}{info['cpu'][:50]}{Colors.END}",
            ]
            
            # Print each system info line centered
            for line in sys_info_lines:
                print(self.center_text(line))
            
            print()
        
        # Quote of day
        if self.config['show_quotes']:
            quote = self.get_quote()
            if quote:
                # Center quote section
                quote_section = [
                    f"{Colors.BRIGHT_GREEN}{Colors.GREEN}[{Colors.WHITE}QUOTE OF THE DAY{Colors.GREEN}]{Colors.END}",
                    f"{Colors.GRAY}---------------------{Colors.END}",
                ]
                
                # Wrap quote if too long
                max_width = 76
                words = quote.split()
                lines = []
                current_line = ""
                
                for word in words:
                    if len(current_line + word) < max_width:
                        current_line += word + " "
                    else:
                        lines.append(current_line.strip())
                        current_line = word + " "
                lines.append(current_line.strip())
                
                for i, line in enumerate(lines):
                    if i == len(lines) - 1:
                        quote_section.append(f"{Colors.BRIGHT_GREEN}{Colors.END} {Colors.WHITE}{line}{Colors.END}")
                    else:
                        quote_section.append(f"{Colors.BRIGHT_GREEN}{Colors.END} {Colors.WHITE}{line}{Colors.END}")
                
                # Print centered quote section with padding
                for line in quote_section:
                    print(self.center_text(line))
                print()
        
        # Current time and date
        current_time = datetime.now().strftime('%H:%M:%S')
        date_str = datetime.now().strftime('%A, %B %d, %Y')
        timestamp = f"{Colors.BRIGHT_PURPLE}[{Colors.BRIGHT_CYAN}{date_str}{Colors.BRIGHT_PURPLE}] [{Colors.BRIGHT_CYAN}{current_time}{Colors.BRIGHT_PURPLE}]{Colors.END}"
        print(self.center_text(timestamp))
        
        print()
        print(self.center_text(divider))
        print()

def main():
    """Main function"""
    try:
        splash = TerminalSplash()
        splash.display()
        
        # Ask for system update
        if splash.config.get('ask_update', True):
            # Detect package manager
            package_managers = {
                'pacman': ['sudo', 'pacman', '-Syu'],
                'apt': ['sudo', 'apt', 'update', '&&', 'sudo', 'apt', 'upgrade'],
                'dnf': ['sudo', 'dnf', 'upgrade'],
                'yum': ['sudo', 'yum', 'update']
            }
            
            pm = None
            for manager in package_managers.keys():
                try:
                    subprocess.run(['which', manager], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                    pm = manager
                    break
                except:
                    continue
            
            if pm:
                response = input(f"{Colors.YELLOW}[?]{Colors.END} Update system packages using {pm}? {Colors.GRAY}(y/N){Colors.END}: ")
                
                if response.lower() in ['y', 'yes']:
                    print(f"\n{Colors.BRIGHT_CYAN}[*]{Colors.END} Running system update...")
                    print(f"{Colors.YELLOW}Note: You may need to enter your password and confirm updates{Colors.END}")
                    subprocess.run(package_managers[pm])
                else:
                    print(f"{Colors.GRAY}[*] Skipping update{Colors.END}")
        
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Interrupted{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        sys.exit(1)

if __name__ == "__main__":
    main()
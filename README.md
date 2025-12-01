# Terminal Splash Screen - Professional Hacker Edition

A sleek, cyberpunk-themed welcome screen for your terminal that displays system information, inspirational quotes, and provides a professional hacker aesthetic.

## Features

- **Cyberpunk ASCII Art**: Anonymous hacker mask with purple/cyan color scheme
- **System Information Display**: Real-time system stats including:
  - User and hostname
  - OS and kernel information
  - Shell environment
  - System uptime
  - Memory usage
  - CPU information
- **Inspirational Tech Quotes**: Random hacker/tech quotes
- **Configurable Settings**: JSON-based configuration system
- **Package Manager Integration**: Optional system update prompts
- **Cross-Platform**: Works on Linux, macOS, and Windows

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lordhanya/terminal-splash-screen.git
cd terminal-splash-screen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Make the script executable (optional):
```bash
chmod +x terminal_splash.py
```

## Usage

Run the script directly:
```bash
python3 terminal_splash.py
```

Or if made executable:
```bash
./terminal_splash.py
```

## Configuration

The script creates a configuration file at `~/.config/terminal_splash/config.json` with the following options:

```json
{
    "show_quotes": true,
    "show_system_info": true,
    "ask_update": true,
    "ascii_style": "cyberpunk"
}
```

- `show_quotes`: Display inspirational tech quotes
- `show_system_info`: Show system information panel
- `ask_update`: Prompt for system package updates
- `ascii_style`: ASCII art style (currently only "cyberpunk")

## Adding to Shell

To run this splash screen automatically when opening a terminal, add one of the following to your shell configuration file:

### Bash (`~/.bashrc` or `~/.bash_profile`):
```bash
python3 /path/to/terminal_splash.py
```

### Zsh (`~/.zshrc`):
```bash
python3 /path/to/terminal_splash.py
```

### Fish (`~/.config/fish/config.fish`):
```fish
python3 /path/to/terminal_splash.py
```

## Requirements

- Python 3.6+
- requests library
- Standard Unix/Linux utilities (for system information)

## Screenshots

*(Add screenshots here when you have them)*

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various terminal splash screen projects
- ANSI color codes for terminal styling
- System information gathering techniques

## Author

Created by Ashif - (https://github.com/lordhanya)
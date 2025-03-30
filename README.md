# Reverse Shell Command Generator

A Python utility for generating various reverse shell commands for cybersecurity professionals, penetration testers, and security researchers.

## Overview

This tool provides a simple command-line interface to generate reverse shell commands for multiple programming languages and tools. It's designed to assist security professionals during authorized penetration testing engagements and security assessments.

## Features

- Generate reverse shell commands for various languages and tools:
  - Bash
  - Perl
  - Python
  - PHP
  - Ruby
  - Netcat (both traditional and alternative methods)
  - PowerShell
- URL encoding option for bypassing certain filters
- Base64 encoding option for obfuscation
- Easy-to-use command-line interface

## Installation

```bash
git clone https://github.com/yourusername/reverse-shell-generator.git
cd reverse-shell-generator
chmod +x reverse_shell_generator.py
```

## Usage

Basic usage:

```bash
./reverse_shell_generator.py <IP> <PORT>
```

Generate a specific type of reverse shell:

```bash
./reverse_shell_generator.py <IP> <PORT> --type bash
```

URL encode the output:

```bash
./reverse_shell_generator.py <IP> <PORT> --url-encode
```

Base64 encode the output:

```bash
./reverse_shell_generator.py <IP> <PORT> --base64
```

### Examples

Generate all reverse shell commands targeting 192.168.1.100 on port 4444:

```bash
./reverse_shell_generator.py 192.168.1.100 4444
```

Generate only a Python reverse shell:

```bash
./reverse_shell_generator.py 192.168.1.100 4444 --type python
```

## Disclaimer

This tool is provided for educational and professional security testing purposes only. Usage of this tool for attacking targets without prior mutual consent is illegal. The developers are not responsible for any misuse or damage caused by this program.

Always ensure you have explicit permission before using these commands on any system or network.

## Legal and Ethical Use

- Only use on systems you own or have explicit permission to test
- Follow responsible disclosure practices
- Adhere to all applicable laws and regulations
- Respect privacy and data protection requirements

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

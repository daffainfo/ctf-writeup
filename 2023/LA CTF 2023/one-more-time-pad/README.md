# one-more-time-pad
> I heard the onetime pad is perfectly secure so I used it to send an important message to a friend, but now a UCLA competition is asking for the key? I threw that out a long time ago! Can you help me recover it?

## About the Challenge
We were given a Python code, and it will look like this

```python
from itertools import cycle
pt = b"Long ago, the four nations lived together in harmony ..."

key = cycle(b"lactf{??????????????}")

ct = ""

for i in range(len(pt)):
    b = (pt[i] ^ next(key))
    ct += f'{b:02x}'
print("ct =", ct)

#ct = 200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e
```

This code generates a repeating key from the string `lactf{??????????????}` by converting it to a sequence of bytes, and uses this key to encrypt a plaintext message "Long ago, the four nations lived together in harmony ..." by XOR-ing it with the key. The resulting ciphertext is a hexadecimal string and is printed.

And we need to find the key

## How to Solve?
To solve this chall, i create a python code to bruteforce the key
```python
from itertools import cycle
import itertools

ct = "200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e"
characters = "abcdefghijklmnopqrstuvwxyz0123456789_"
for combination in itertools.product(characters, repeat=1):
    strings = "lactf{" + ''.join(combination) + "}"
    key = cycle(bytes(strings, encoding='utf-8'))
    pt = ""

    for i in range(0, len(ct), 2):
        hex_char = ct[i:i+2]
        b = int(hex_char, 16) ^ next(key)
        pt += chr(b)
    
    print(strings , pt)
```

This code generates all possible combinations of the characters `abcdefghijklmnopqrstuvwxyz0123456789_` of length 1, adds the prefix `lactf{` and the suffix `}` to form a string, converts the string to a sequence of bytes, and uses this sequence of bytes as a key to decrypt a hex-encoded ciphertext `ct` by repeating it and XOR-ing it with the ciphertext. The decrypted plaintext is then appended to each generated string and both are printed.

> Well, the python code is not perfect because I still need to verify its output (But at least the code works XD)
```
lactf{b4by_h1t_m3_0ne_m0r3_t1m3}
```
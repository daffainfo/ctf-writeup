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
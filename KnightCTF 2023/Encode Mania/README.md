# Encode Mania
> Encoding random stuffs is so cool! I just want to encode it over and over and over again ...

## About the Challenge
We have been given a python script to encrypt the flag and the encrypted file. And if we open the script, the script will be look like this

```python
import base64
from random import randint

flag = "kctf{************}"

def encrypt(s, option):
    if option == 0:
        ret = base64.b64encode(s)
    elif option == 1:
        ret = base64.b32encode(s)
    elif option == 2:
        ret = base64.b16encode(s)
    else:
        ret = base64.b85encode(s)

    return ret


encrypted_flag = flag.encode('utf-8')

for _ in range(12):
    option = randint(0, 3)
    encrypted_flag = encrypt(encrypted_flag, option)

with open("encode_mania.txt", 'w') as f:
    f.write(encrypted_flag.decode())
```
The program will encode the flag 12 times with different random encoding (base64, base32, base16, and base85) as you can see in this line (You can get the script [**here**](/KnightCTF%202023/Encode%20Mania/encrypt.py))
```python
for _ in range(12):
    option = randint(0, 3)
    encrypted_flag = encrypt(encrypted_flag, option)
```

## How to Solve?
To solve this i created a python script to bruteforce each possibility 12 times with all encoding (You can get the script [**here**](/KnightCTF%202023/Encode%20Mania/decrypt.py))
```python
import base64
import re

encoded_flag = "GUZDGMRUIQ3T......"
def decrypt(s, option):
    if option == 0:
        ret = base64.b64decode(s)
    elif option == 1:
        ret = base64.b32decode(s)
    elif option == 2:
        ret = base64.b16decode(s)
    else:
        ret = base64.b85decode(s)
    return ret

for _ in range(12):
    for option in range(4):
        try:
            dec = decrypt(encoded_flag, option)
            if re.findall(r"^\w+", dec.decode()):
                print(dec.decode())
            encoded_flag = dec.decode()
        except:
            pass
```
And the flag will be printed in the terminal
```
KCTF{dfs_0r_b4u7e_f04ce}
```
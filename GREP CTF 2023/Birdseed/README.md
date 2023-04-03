# Birdseed
> Now that my program is truly random, you'll never be able to guess the flag.

## About the Challenge
We have been given 2 files:
* [encrypt.py](encrypt.py)
* [out.txt](out.txt)

Here is the content of `encrypt.py` file
```python
import random
flag = open('flag.txt').read()

rand_seed = random.randint(0, 999)
random.seed(rand_seed)
encrypted = ''

for chr in flag:
    encrypted += f'{(ord(chr) ^ random.randint(0, 255)):02x}'

with open('out.txt', 'w') as f:
    f.write(encrypted)
```

This Python code reads the contents of a file named 'flag.txt' and encrypts it using a simple XOR cipher with a random seed generated using the `random.randint()` function

## How to Solve?
As you can see in the `encrypt.py` file, the seed is not really random because that function only generate a random integer between 0 and 999. So to solve I have created the script to bruteforce the seed from 0 to 1000

```python
import random
encrypted = "a282b415279f5aa08cd4649515268910b8968a1eabda7c1bb2898c"

for rand_seed in range(1, 1001):
    random.seed(rand_seed)

    flag = ''
    for i in range(0, len(encrypted), 2):
        xor_val = int(encrypted[i:i+2], 16)
        flag += chr(xor_val ^ random.randint(0, 255))

    print("The flag is:", flag)
```

And im using `grep` too to find the flag. Here is the final command that I used

```shell
python3 solve_bird.py | grep "grepCTF" -a
```

![flag](images/flag.png)

```
grepCTF{n3v3r_tru1y_r4nd0m}
```
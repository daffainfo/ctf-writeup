# CaeX0R 2
> Ooops, i forgot the shift this time. Can you still figure out my flag.

## About the Challenge
We have been given a file to encrypt the flag (You can download the file [here](enc.py))

Here is the content of `enc.py` file
```python
#enc.py
from random import *
flag="REDACTED"
a=randint(1,1000)
c=[]
for f in flag:
   c.append(str(ord(f)^a))
print(c)
print(a)

#c=['313', '296', '295', '304', '274', '280', '263', '280', '263', '310', '315', '310', '316', '345', '268', '263', '310', '302', '345', '296', '276']
#a=REDACTED
```

This Python code defines a script that performs a simple encryption on a flag using XOR cipher. The encryption key is a random integer between 1 and 1000 generated using the `randint()` function from the random module.

## How to Solve?
As you can see in the `enc.py` file, the seed is not really random because that function only generate a random integer between 0 and 1000. So to solve I have created the script to bruteforce the key from 0 to 1000

```python
from random import *
import itertools

c = ['313', '296', '295', '304', '274', '280', '263', '280', '263', '310', '315', '310', '316', '345', '268', '263', '310', '302', '345', '296', '276']

for a in range(1, 1001):
    flag = ""
    for char_code in c:
        char_code = int(char_code)
        char = chr(char_code ^ a)
        flag += char
    
    print(flag)
```

And im using `grep` too to find the flag. But in this case we can't find the flag directly, but I will search for the string containing the characters `{` and `_`

```shell
python3 solve_caex0r2.py | grep "{" -a | grep "_"
```

![grep](images/grep.png)

As you can see `PANY{qnqn_R_U0en_G0A}` was interesting because it match with the flag structure, So i put that string into caesar cipher decoder (You can use [dcode.fr](https://www.dcode.fr/caesar-cipher) to do this)

![flag](images/flag.png)

```
GREP{hehe_I_L0ve_X0R}
```
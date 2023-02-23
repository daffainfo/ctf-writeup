# Feb. 7 - Better Notes
> Okay, so maybe my super-secure method was a bust. But I'm persistent (actually, I'm Sam)! I've written another program, and this time, there aren't any pesky keys to keep (KEYp 🙃) track of! I wrote you another Valentine that my program encrypts as `WU]Wipuk\cYAvtEXHsRlP_YlPs[UMtVmkcOjupFCVGU`.

> The `valentine{...}` wrapper is included in the encrypted text.

## About the Challenge
We have been given a python code, and the code will look like this
```python
from base64 import b64encode

valentine = bytes(input("Valentine: "), "utf-8")
a = b64encode(valentine)
b = b64encode(valentine[::-1])
a = list(map(ord, list(str(a))))
b = list(map(ord, list(str(b))))
for j in range(len(a)):
  print(chr((a[j] + b[j]) % 58 + 65), end='')
print("")
```

The valentine bytes are encoded using base64 using the `b64encode` function from the base64 module. The resulting encoded bytes are stored in the variable `a`. The valentine bytes are reversed using the slice notation `[::-1]`, then encoded using base64 and stored in the variable b. The a and b variables are converted to lists of integers using the list and `map` functions. Specifically, the `list(str(a))` and `list(str(b))` expressions convert the base64-encoded bytes to strings, and then the map`(ord, ...)` function maps the ord function to each character in the string, which converts it to its corresponding ASCII code. The program then iterates over the length of a (which should be the same as the length of b) using a for loop. For each iteration of the loop, the program adds the corresponding a and b elements together and takes the result modulo 58. The result is then added to 65, which converts it to a character code in the range A to z. The resulting character code is converted to a character using the chr function and printed to the console using the end argument of the print function to prevent a newline character from being printed.

## How to Solve?
One of the team members already got some parts of the flag.
```
WU]Wipuk\cYAvtIT`sXlP_YlPswUMtVmkcOjupFCVGU valentine{c0ltHmqbAAnky_f4ce}
```
And then i bruteforce the flag using this code (And doing a little bit guessing haha)

```python
from base64 import b64encode
import itertools

chara = ["if","is","it","in","of","or","at","as","be","by","do","go","he","me","my","no","oh","on","so","to","up","us","we"]
characters = "abcdefghijklmnopqrstuvwxyz0123456789_"
for combinations in chara:
  for combination in itertools.product(characters, repeat=3):
    strings = "valentine{t" + ''.join(combination) + "_" + combinations + "_w1nky_f4ce}"
    valentine = bytes(strings, encoding="utf-8")
    a = b64encode(valentine)
    b = b64encode(valentine[::-1])
    a = list(map(ord, `list(str(a))`))
    b = list(map(ord, list(str(b))))
    for j in range(len(a)):
      print(chr((a[j] + b[j]) % 58 + 65), end='')
    print(" " + strings)
```
After running this code for a while, we can get the flag
```
valentine{t3xt_me_w1nky_f4ce}
```
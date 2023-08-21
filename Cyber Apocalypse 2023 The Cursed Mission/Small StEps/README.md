# Small StEps
> As you continue your journey, you must learn about the encryption method the aliens used to secure their communication from eavesdroppers. The engineering team has designed a challenge that emulates the exact parameters of the aliens' encryption system, complete with instructions and a code snippet to connect to a mock alien server. Your task is to break it.

## About the Challenge
We have been given a zip file (You can download the file [here](crypto_small_steps.zip)). And if we unzip the file, there are another file called `solver.py` and `server.py`. Here is the content of `server.py`

```python
from Crypto.Util.number import getPrime, bytes_to_long

FLAG = b"HTB{???????????????}"
assert len(FLAG) == 20


class RSA:

    def __init__(self):
        self.q = getPrime(256)
        self.p = getPrime(256)
        self.n = self.q * self.p
        self.e = 3

    def encrypt(self, plaintext):
        plaintext = bytes_to_long(plaintext)
        return pow(plaintext, self.e, self.n)


def menu():
    print('[E]ncrypt the flag.')
    print('[A]bort training.\n')
    return input('> ').upper()[0]


def main():
    print('This is the second level of training.\n')
    while True:
        rsa = RSA()
        choice = menu()

        if choice == 'E':
            encrypted_flag = rsa.encrypt(FLAG)
            print(f'\nThe public key is:\n\nN: {rsa.n}\ne: {rsa.e}\n')
            print(f'The encrypted flag is: {encrypted_flag}\n')
        elif choice == 'A':
            print('\nGoodbye\n')
            exit(-1)
        else:
            print('\nInvalid choice!\n')
            exit(-1)


if __name__ == '__main__':
    main()
```

As we can see, the public exponent is very small (3) and we only have an information about the ciphertext, public exponent, and the public key

## How to Solve?
Im using [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool) to solve the chall, here is the command I used

```bash
python3 RsaCtfTool.py -n 7079390432974855345319643397277546809126929622683749677273378219032261712283081531451428558847051155395790169332117706417782515882054955482729948765182401 -e 3 --uncipher 70407336670535933819674104208890254240063781538460394662998902860952366439176467447947737680952277637330523818962104685553250402512989897886053
```

Wait for a while and you will get the flag

![flag](images/flag.png)

```
HTB{5ma1l_E-xp0n3nt}
```
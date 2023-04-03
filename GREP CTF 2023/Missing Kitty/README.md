# Missing Kitty
> My kitty is missing. Can you find her ? Last seen saying meow meow under the blanket !!

## About the Challenge
We have been given a file (You can download the file [here](Missing.jpg)) and we need to find the flag using that picture

## How to Solve?
To solve this, Im using `stegseek` first to extract hidden data from files by performing bruteforce attack. Here is the command to bruteforce the image using `rockyou.txt` wordlist

```shell
stegseek Missing.jpg /usr/share/wordlists/rockyou.txt
```

![stegseek](images/stegseek.png)

We got txt file. If we open the file, we got this message

```
Dk what's this, some kitten language

memmemmmmeemmememeemeemmmeemeemmmeemeeeemmemmmmmmeemeememeeeemmemmemmmmmmeememeemeememmemeeememmmeeememmmeeeemmemmemeemmmmmmememmmmmememmemmmeemmeememmemeemeeemmeemmmmemeemeemmmeemeemmmeeeemmemmemmmmmmeeeemmemeemeeeemeeemememmemmmmmmeemmeemmeemeeeemeeemememeemeeemmeemmemmmmemmmmmmeememmmmeemmememeeemmemmmemeeemmmemmmmmmemmemmemmemmmmmmeemmmmemeemeememmemmmmmmeemmemmmeemmememeemeemmmeememmemeemmeeemeememmmmeeememmmeemmememeemmemmmmemeeemmmmmememmmmmememmemememmmeemmmmemeememeemeemmememmemmmmmmeememmemeeememmmmemeemmmmemmmmmmeememmmmeemmememeeemmemmeemmememmemmeeemeeemmeemmemmmmmmeeeemmemeemeeeemeeemememeeemmemmmemmmmmmeemmeeemeememmemeemmeemmeeememmmmmmememmeemmeemmeemeemmmeemmmmemeemmeeemmemmmmmmmeeememmmemmmmmmeeeemeemememmeemeeemeeemmeemmeemmeemmeemeeememmmemeeeeemeemeemmmmeemmmemeeememmmeeememmmeemeemmmeemmemememeeeeemeememeemmeemmmemeeememmmeeememmmmeemmeemeemeeemmeeeeeme
```

Change the character `m` to 0 and character `e` to 1. And then decode the binary to obtain the flag

![flag](images/flag.png)

```
GREP{steghide,Sw33t_l1ttle_k1tt3n}
```
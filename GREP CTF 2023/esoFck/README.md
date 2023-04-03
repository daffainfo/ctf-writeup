# esoF*ck
> I've heard about brainf#ck but what the f#ck js this?

## About the Challenge
We have been given a file (You can download the file [here](msg.txt)) and we need to decode it to obtain the flag

## How to Solve?
First, we need to remove `f#ck` keyword from the msg, and then here is the result

![remove](images/remove.png)

And then find JSFuck decoder (In this case, im using [dcode.fr](https://www.dcode.fr/jsfuck-language)) and here is the output

![flag](images/flag.png)

```
grepCTF{3sot3r1c_l4ngu4g3s_ftw}
```
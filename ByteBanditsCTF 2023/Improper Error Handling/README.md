# Improper Error Handling
> This website is giving errors. Can you figure it out ?

## About the Challenge
We are given a [web](http://web.bbctf.fluxus.co.in:1001/) where we can enter a `password` in the form. If the string is too short, an error will occur. However, if the string is long enough, the website will produce an encoded string.

![preview](images/preview.png)

## How to Solve?
We just need to find the character limit so that the website doesn't produce an error. A string with 32 characters will reveal the flag. (For example AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)

```
BBCTF{tHis_i5_1t_Y0u_CraCk3D_iT}
```
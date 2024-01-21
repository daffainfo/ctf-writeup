# ERaaS
> Emergency response? Afraid not

## About the Challenge
We were given a website without the source code, where the website only has one functionality: converting the epoch to date.

![preview](images/preview.png)

## How to Solve?
The website is vulnerable to OS Command Injection through the addition of `;` after the epoch, followed by the command you want to execute

![ls](images/ls.png)

![flag](images/flag.png)

```
nite{b3tt3r_n0_c5p_th7n_b7d_c5p_r16ht_fh8w4d}
```
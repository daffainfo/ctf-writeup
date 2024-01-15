# baby-rsa
> small numbers for small messages

## About the Challenge
We were given a file that contain a modulus, public exponent, and ciphertexts (You can download the file [here](output.txt))

```
n = 10888751337932558679268839254528888070769213269691871364279830513893837690735136476085167796992556016532860022833558342573454036339582519895539110327482234861870963870144864609120375793020750736090740376786289878349313047032806974605398302398698622431086259032473375162446051603492310000290666366063094482985737032132318650015539702912720882013509099961316767073167848437729826084449943115059234376990825162006299979071912964494228966947974497569783878833130690399504361180345909411669130822346252539746722020515514544334793717997364522192699435604525968953070151642912274210943050922313389271251805397541777241902027
e = 3
c = 2449457955338174702664398437699732241330055959255401949300755756893329242892325068765174475595370736008843435168081093064803408113260941928784442707977000585466461075146434876354981528996602615111767938231799146073229307631775810351487333
```

As you can see the public exponent was very small

## How to Solve?
In this case im using [X-RSA](https://github.com/X-Vector/X-RSA) to recover the plaintext, and because then choose the 13th option

![flag](images/flag.png)

```
tjctf{thr33s_4r3_s0_fun_fb23d5ed}
```
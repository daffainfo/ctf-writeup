# Super Admin
> Comfort food.

## About the Challenge
We were given a website without a source code, and we need to login as admin in order to get the flag

![preview](images/preview.png)

![preview2](images/preview2.png)

## How to Solve?
Because there is a JWT token in the website cookie, You can use jwt.io to inspect the cookie

![old_jwt](images/old_jwt.png)

We need to change `"role": "user"` to `"role": "admin"`, but we need to know the password first. The first thing that came to my mind was bruteforcing the key. I used https://github.com/Sjord/jwtcrack to crack the password. Here is the result:

```
Cracking JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciIsImlhdCI6MTY5ODY2NTMzNX0.yozk78J3cGuLt1ofBxUCnUoagoR9wOxXoA30o3hh6ug
27it [00:00, 12833.89it/s]
Found secret key: password1
```

Change the value from `user` to `admin` using the cracked password

![new_jwt](images/new_jwt.png)

Replace the old token with the new JWT token to obtain the flag

![flag](images/flag.png)

```
UDCTF{k33p_17_51mp13_57up1d_15_4_l1e}
```
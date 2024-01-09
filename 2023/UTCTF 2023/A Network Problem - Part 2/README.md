# A Network Problem - Part 2
> Update: smb port has been moved to 8445 from 445 on networking-misc-p2

> betta.utctf.live has other interesting ports. Lets look at 8445 this time.

## About the Challenge
We were given a SMB server to connect `betta.utctf.live:8445`

## How to Solve?
To get the flag you need to connect to the server using `smbclient` because this is SMB protocol. You don't need an username and password because the server allow anonymous login. First you need to know the `Sharename` on the server. You can use this command

```
smbclient --no-pass -L //betta.utctf.live
```

![sharename](images/sharename.png)

And then I connect to `WorkShares` using this command

```
smbclient -U '%' -N \\\\betta.utctf.live\\WorkShares
```

Go to `shares\IT\Itstuff\` and get the `notetoIT` file to get the flag

![get](images/get.png)

Here is the content of the file
```
I don't understand the fasination with the magic phrase "abracadabra", but too many people are using them as passwords. Crystal Ball, Wade Coldwater, Jay Walker, and Holly Wood all basically have the same password. Can you please reach out to them and get them to change thier passwords or at least get them append a special character? 

-- Arty F.

utflag{out-of-c0ntrol-access}
```

```
utflag{out-of-c0ntrol-access}
```
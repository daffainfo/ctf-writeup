# Compromised Account

> Which user account was compromised? What was the username & password?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `Login Successful` like this

![POC 1](images/POC%201.jpg)

The password has been found, it seems `tareq@nanomate`

Next is we find the username with filter string `tareq`

![POC 2](images/POC%202.jpg)

Because the format is `BDSEC{username_password}`

Then flag is

```
BDSEC{tareq_tareq@nanomate}
```
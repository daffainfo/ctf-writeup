# Compromised Admin Account

> What is the admin password?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `Login Successful` like this

![POC 1](images/POC%201.jpg)

Seem there only this root user as admin then the password is `41528ac7f116e9661cf57be7cd79e1a2`

Because the format is `BDSEC{password}`

Then flag is

```
BDSEC{41528ac7f116e9661cf57be7cd79e1a2}
```
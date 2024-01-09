# Root Permission

> What binary had the root permission?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `Linux` like this

![POC 1](images/POC%201.jpg)

Seem the binary for the privilege escalation to root is `vim`

Because the format is `BDSEC{Flag}`

Then flag is

```
BDSEC{vim}
```
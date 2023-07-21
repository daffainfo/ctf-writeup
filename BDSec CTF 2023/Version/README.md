# Version

> What is the Linux version of the server?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `Linux` like this

![POC 1](images/POC%201.jpg)

Seem the version is `5.19.0-46-generic`

Because the format is `BDSEC{versi-on}`

Then flag is

```
BDSEC{5.19.0-46-generic}
```
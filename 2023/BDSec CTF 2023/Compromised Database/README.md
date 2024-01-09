# Compromised Database

> How did the attacker enumurate & compromised the database?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `UNION` because according the description database is more like SQL Injection POC

![POC 1](images/POC%201.jpg)

Then we look the header of request

![POC 2](images/POC%202.jpg)

Because the format is `BDSEC{name/version}`

Then flag is

```
BDSEC{sqlmap/1.6.10#stable}
```
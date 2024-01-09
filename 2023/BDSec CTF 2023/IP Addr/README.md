# IP Addr
> Nanomate Solutions, a dynamic startup software development company, has unfortunately experienced a recent security breach resulting in unauthorized access to their database. In response to this incident, the company's Incident Response team has obtained the network packet file and is seeking your expertise to investigate the evidence. Your skills are crucial in securing the company and resolving this matter effectively. Join forces with the Incident Response team to protect Nanomate Solutions and secure their confidence in their system's integrity.

> What is the server & attacker ip?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request like this

![POC 1](images/POC%201.jpg)

Because the format is `BDSEC{serverip_attackerip}`

Then flag is

```
BDSEC{192.168.1.5_192.168.1.7}
```
# Database Flag

> What binary had the root permission?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `Task Title`

![POC 1](images/POC%201.jpg)

Because the format is `BDSEC{flag}`

Then flag is

```
BDSEC{Dev3L0peR_sH0uLD_n3veR_TrusT_uSer_InPuT}
```
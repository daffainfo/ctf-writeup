# Was it Vulnerable?

> Was Process Task Details page vulnerable? If yes, what was the vulnerability?

Download the pcap file [here](file/challenge.zip)

# How to Solve

We need look the pcap file and see the http request with filter string `profile.php`

![POC 1](images/POC%201.jpg)

After check the request is likely the attacker can view the other task, which is this vulnerability called `IDOR`

And then filter string with `UNION`

![POC 2](images/POC%202.jpg)

This surely `SQLI` request

Because the format is `BDSEC{VULN_VULN}`

Then flag is

```
BDSEC{IDOR_SQLI}
```
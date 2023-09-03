# Rogueful Helper
> The DUC Corp security team began receiving alerts for reconaissance activity from a newly installed workstation. Analysts have put together a brief investigation package for triage.

> What was the ICMP Payload used for the task that finished 2023-08-26 15:32:20?. Flag format: DUCTF{payload}

## About the Challenge
We received a very large zip file, which contains several folders from drive C: in Windows.

![preview](images/preview.png)

And we need to find the ICMP payload

## How to Solve?
To solve this problem, im using `grep` command and grep the date like this

```bash
grep -r "15:32:20" . -a -b2
```

It will search for the string `15:32:20` in all files (including binary files) within the current directory and its subdirectories.

![grep](images/grep.png)

Hmmm, we found something at `./Program Files/VSA X/Probe/audit.s3db`. Lets check the file

![payload](images/payload.png)

You can see 2 interesting lines inside this file

```
-icmppayload
cHd5cmVxAWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWE=
```

The ICMP payload is `cHd5cmVxAWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWE=`. Now, wrap it in DUCTF{}.

```
DUCTF{cHd5cmVxAWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWE=}
```
# Attaaaaack1
> One of our employees at the company complained about suspicious behavior on the machine, our IR team took a memory dump from the machine and we need to investigate it.

> Q1. What is the best profile for the the machine?

> example : crew{Profile}

## About the Challenge
We got `raw` image and we need to find the profile using Volatility2

## How to Solve?
To solve this, we need to find the best profile using `imageinfo` plugin. Here is the command that I used

```
vol.py -f /path/to/memdump.raw imageinfo
```

![flag](images/flag.png)

```
crew{Win7SP1x86_23418}
```
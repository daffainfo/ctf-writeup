# Attaaaaack4
> Q4. What is the name and PID of the suspicious process ?

> example : crew{abcd.exe_111}

## About the Challenge
We got `raw` image and we need to find the suspicious process and also the pid

## How to Solve?
To solve this, we need to find the suspicious process using `pslist` plugin. Here is the command I used

```
vol.py -f /path/to/memdump.raw --profile=Win7SP1x86_23418 pslist
```

![flag](images/flag.png)

You will notice there is a suspicious proccess called `runddl.exe`. Why suspicious? because the program has a typo, not `rundll.exe` but `runddl.exe`

```
crew{runddl.exe_2556}
```
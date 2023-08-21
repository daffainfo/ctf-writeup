# Attaaaaack5
> Q5. What is the another process that is related to this process and it's strange ?

> example : crew{spotify.exe}

## About the Challenge
We got `raw` image and we need to find the child process

## How to Solve?
To solve this, we need to find the child process using `pstree` plugin. Here is the command I used

```
vol.py -f /path/to/memdump.raw --profile=Win7SP1x86_23418 pstree
```

![flag](images/flag.png)

Or you can use `pslist` plugin and then look for the process whose parent pid is 300

```
crew{notepad.exe}
```
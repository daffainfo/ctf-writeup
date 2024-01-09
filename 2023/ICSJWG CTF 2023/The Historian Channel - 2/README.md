# The Historian Channel - 2
> Jubilife’s SOC looked for other suspicious events around the time of the successful brute force login and noticed earlier activity from the suspicious user (IP address 192.168.4.146) in the web server logs. It looks like this user attempted to access information on the webserver without logging in, and it is possible that they succeeded in reading files they were not supposed to have access to due to a misconfiguration.

> What is the name of the file (full path) that the suspicious user accessed from the webserver?

> Flag format: full path of file. Example: if the file accessed was /folder/file.txt, the flag would be /folder/file.txt

## About the Challenge
We were given a log file to analyze (You can download the file [here](access.log)). And we need to find the full path of the file that the user accessed

## How to Solve?
If we check on the log file, there are some suspicious request that the suspicious user trying to find some configuration files such as `config.txt` or `config.ini`

![flag](images/flag.png)

As you can see, some of the requests returned a `404 Error`. However, when the user accessed `/jubilifehistorian/config.ini`, it returned a `200 OK` status code.

```
/jubilifehistorian/config.ini
```
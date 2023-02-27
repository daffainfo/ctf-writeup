# Docker Web
`-`

## About the Challenge
We are given a zip code that contain linux directories

![preview](images/preview.png)

## How to Solve?
Open the `index.html` file on `/var/www/html` directories and you will notice there is a base64 encoded msg in line `21`

![base64](images/base64.png)

And if you decode it, you will get the flag

```
vu-cyberthon-23
```
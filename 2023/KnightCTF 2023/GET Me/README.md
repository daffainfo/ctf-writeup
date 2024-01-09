# GET Me
> Can you GET the flag from the API ?

## About the Challenge
We were given a website, and if we open the website the response like this

```json
{
    "success":false,
    "message":"Sorry ! You can't GET it :P"
}
```

## How to Solve?
First i tried to change the HTTP request method from `GET` to `POST`. And then here is the response

```json
{
    "success":false,
    "message":"You should send me a url !"
}
```
And then i tried to add a parameter named `url` and the value of the parameter i just using random url, for example https://google.com. And here is the response.

```json
{
    "success":false,
    "message":"Looking for flag ? Visit https:\/\/hackenproof.com\/user\/security"}
```

And after stuck a little bit, i open hackenproof and register to that website and secured the the flag
```
KCTF{H4ck3nPr00f3d_bY_Kn16h75qu4d}
```
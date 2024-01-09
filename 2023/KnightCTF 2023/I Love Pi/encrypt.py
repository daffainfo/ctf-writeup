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
import base64
import re

encoded_flag = "GUZDGMRUIQ3T......"
def decrypt(s, option):
    if option == 0:
        ret = base64.b64decode(s)
    elif option == 1:
        ret = base64.b32decode(s)
    elif option == 2:
        ret = base64.b16decode(s)
    else:
        ret = base64.b85decode(s)
    return ret

for _ in range(12):
    for option in range(4):
        try:
            dec = decrypt(encoded_flag, option)
            if re.findall(r"^\w+", dec.decode()):
                print(dec.decode())
            encoded_flag = dec.decode()
        except:
            pass
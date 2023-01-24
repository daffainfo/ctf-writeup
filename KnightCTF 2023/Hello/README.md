# Hello
> Sir vignere came to my dreams and sent me this packet capture and told me to find the flag from it which is the key to my success. I am a noob in these cases. So I need your help. Please help me find the flag. Will you?

## About the Challenge
We have been given a `pcapng` file and we need to open the file in wireshark

## How to Solve?
If we open the file in wireshark and if we check on the DNS packet, there is a single character on each packet

![wireshark](images/wireshark.png)

After we arrange the character, here is the result
```
VVBCTHtvMV9tcjNhX2VuMF9oazNfaTBofQ==
```
And we know that's base64 encode! But after we decode the encoded text the result is
```
UPBL{o1_mr3a_en0_hk3_i0h}
```
And then because there is a hint in the question "`Sir vignere came to ...`". Decode the msg with vigenere cipher and the key is `KNIGHT`
```
KCTF{h1_th3n_wh0_ar3_y0u}
```
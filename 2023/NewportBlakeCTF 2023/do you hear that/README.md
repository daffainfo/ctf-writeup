# do you hear that?
> I'm not sure why, but when I look at this image I can hear some sort of faint sound. Do you hear it too?

## About the Challenge
We were given an image called `help.png` (You can download the file [here](help.png)) and if we check using `zsteg` there's a wav file inside the image

```
root@ubuntu:~# zsteg help.png
[?] 317564 bytes of extra data after image end (IEND), offset = 0x8a24
extradata:0         .. file: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz
    00000000: 52 49 46 46 74 d8 04 00  57 41 56 45 66 6d 74 20  |RIFFt...WAVEfmt |
    00000010: 10 00 00 00 01 00 01 00  44 ac 00 00 88 58 01 00  |........D....X..|
    00000020: 02 00 10 00 64 61 74 61  50 d8 04 00 00 00 00 00  |....dataP.......|
    00000030: 01 00 03 00 05 00 08 00  0a 00 0b 00 0b 00 09 00  |................|
    00000040: 06 00 02 00 fe ff f9 ff  f6 ff f4 ff f5 ff f7 ff  |................|
    00000050: fb ff 00 00 04 00 08 00  09 00 06 00 00 00 f7 ff  |................|
    00000060: ec ff e0 ff d5 ff cd ff  c8 ff c8 ff ce ff d7 ff  |................|
    00000070: e3 ff f0 ff fb ff 03 00  05 00 01 00 f7 ff e9 ff  |................|
    00000080: d8 ff c9 ff be ff b9 ff  bd ff cb ff e0 ff fd ff  |................|
    00000090: 1b 00 39 00 51 00 60 00  64 00 5c 00 4b 00 32 00  |..9.Q.`.d.\.K.2.|
    000000a0: 18 00 02 00 f6 ff f7 ff  08 00 29 00 57 00 8d 00  |..........).W...|
    000000b0: c3 00 f1 00 0e 01 16 01  05 01 db 00 9e 00 55 00  |..............U.|
    000000c0: 0c 00 ce ff a6 ff 9d ff  b7 ff f2 ff 46 00 a4 00  |............F...|
    000000d0: fb 00 36 01 40 01 09 01  88 00 ba ff aa fe 6a fd  |..6.@.........j.|
    000000e0: 17 fc d3 fa c5 f9 10 f9  d2 f8 21 f9 01 fa 6d fb  |..........!...m.|
    000000f0: 4c fd 7b ff cb 01 09 04  04 06 8f 07 89 08 de 08  |L.{.............|
[!] possible image block size is 639x5, downscaling may be necessary
```

## How to Solve?
First, we need to extract the WAV file inside the png using this command

```bash
zsteg -e extradata:0 help.png > sound.wav
```

And then use spectogram analyzer, there's an online tool like https://www.dcode.fr/spectral-analysis or you can use `Sonic Visualizer`

![Flag](images/flag.png)

```
bctf{y0u_h4v3_s0m3_g00d_34rs}
```
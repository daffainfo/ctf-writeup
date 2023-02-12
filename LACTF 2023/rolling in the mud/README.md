# rolling in the mud
> uugh, these pigs in my pen are making a complete mess! They're rolling all over the place!

> Anyway, can you decode this cipher they gave me, almost throwing it at me while rolling around?

> Answer in lowercase with symbols. In the image, { and } are characters that should appear in your flag, and replace spaces with _.

## About the Challenge
We have been given an image and we need to decode the msg

![cipher](images/cipher.png)

## How to Solve?
Its easy, that's a `Pigpen cipher` and we can decode the msg using [this](https://www.dcode.fr/pigpen-cipher) website (We need to rotate the image 180 degrees first)
```
lactf{rolling_and_rolling_and_rolling_until_the_pigs_go_home}
```
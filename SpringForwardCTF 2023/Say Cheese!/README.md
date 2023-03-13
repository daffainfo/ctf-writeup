# Say Cheese!
> This photo was given to us and we believe this man may play an important part into all this craziness. Can you find out what the make and model of the device used to take the selfie was? Flag will be in this format

> nicc{MakeWord1_MakeWord2_ModelWord1_ModelWord2}

## About the Challenge
We have been given a photo and we need to get the flag from the photo (You can download the photo [here](Selfie.jpg))

## How to Solve?
Use tools like `exifdata` to check the metadata of the file

![metadata](images/metadata.png)

There are `make` and `model` metadata. We need to combine them to get the final flag

```
nicc{Security_Camera_Kmart_Special}
```
# Based on the analysis of the video file 20221015_173902.mp4, please provide the GPS coordinates of the possible place, where video was recorded
> Based on the analysis of the video file 20221015_173902.mp4, please provide the GPS coordinates of the possible place, where video was recorded

## About the Challenge
We need to find the location of the video

## How to Solve?
First i export the file from FTK Imager (You can find the file on `/root/media/0/Download` folder)

![preview](images/extract.png)

After that, check the metadata using `exiftool`. There is GPS location in the metadata

![metadata](images/metadata.png)

```
54.8263, 25.4083
```
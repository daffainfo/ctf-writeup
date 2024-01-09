# Hidden Figures
> Look at this fan page I made for the Hidden Figures movie and website! Not everything is what it seems!

## About the Challenge
We've got a website about a movie called `Hidden Figures`

![preview](images/preview.png)

## How to Solve?
At first I got stuck for a very long time because this website was a static website and there is some weird JavaScript file and I still got nothing lol. And then I check every image on the website

```
data:image/png;base64,/9j/4AAQSkZJRgABAQEAlgCWAAD//gBWRmlsZSBzb3VyY2U6IGh0dHA6Ly9jcmdpcy5uZGMubmFzYS5nb3YvY3JnaXMtZWRpdC9pbmRleC5waHAvRmlsZTpHUE4tMjAwMC0wMDE5MzIuanBn/9sAQwAGBAUGBQQGBgUGBwcGCAoQCgoJCQoUDg8MEBcUGBgXFBYWGh0lHxobIxwWFiAsICMmJykqKRkfLTAtKDAlKCko/8AACwgA8AEsAQERAP/EAB0AAAEFAQEBAQAAAAAAAAAAAAUCAwQGBwgBAAn/...
```

And then I tried using `binwalk` on every image, and I found the flag by using the image on line 609.

![flag](images/flag.png)

```
flag{e62630124508ddb3952843f183843343}
```
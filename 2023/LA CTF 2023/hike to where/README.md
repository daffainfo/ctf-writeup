# hike to where
> Where was this photo taken? I think it used to be in the original photo, but someone cropped it out!

> The flag is lactf{location}, where location is the name of the POI that this person hiked up to, all lowercase and replacing spaces with underscrolls. Use the google maps name of the POI: for example, if the solution is the UCLA Bruin Bear statue, this is the google maps location, and the flag would be `lactf{bruin_statue}`.

> Please note: **contacting anyone or any organization beyond official LA CTF support channels regarding this challenge is against the rules. Please be respectful of those who are involved in this challenge.**

## About the Challenge
We were given a people image and we need to know where this photo was taken.

![person](images/person.jpg)

## How to Solve?
First, I tried to find a hiking or backpacking event in America but found nothing. However, when I searched in Google Images using the keyword `ucla computer science`, I found a person named `Carey Nachenberg`.

![googlesearch](images/professor.png)

After that i tried to googling about `Carey Nachenberg hiking event` and I found this event

https://www.tickettailor.com/events/peaksprofessorsatucla/792649

And i tried to submit the flag using that event name and luckily its correct

```
lactf{skull_rock}
```
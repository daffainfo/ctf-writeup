# Name that song 2
> Another song for you - this time in mod format - but no instrument names for you to search up. Same flag format as last challenge.

> Originally depends on: Name that Song 2

## About the Challenge
The purpose of this problem is how to get the title of the song that has been given (Like the previous problem and you can get the song [**here**](/IrisCTF%202023/Name%20that%20song%202/song_2.mod))

## How to Solve?
First i check the metadata of the file, im using https://www.metadata2go.com/ and I got nothing. 

Luckily in modarchive.org there is a filter in the search feature. I set 2 filters.
- Find song that have a file size between 600 and 999 Kb
- Find song that have an extension `.mod`
  
![filters](images/filters.png)

And then I searched through all the genres :D and I found the song
```
irisctf{hit_and_run}
```
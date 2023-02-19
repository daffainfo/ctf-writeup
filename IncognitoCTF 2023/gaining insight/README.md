# gaining insight
`-`

## About the Challenge
We are given an email (kristen@kristenchavis.com) and we need to find a resume

## How to Solve?
One of the team member found the resume in github repository (You can access the resume [here](https://github.com/kristenchavis01/resume/blob/main/resume.tex))

![github](images/github.png)

And then if we check the commit named `Added profile.jpg` (You can access the commit [here](https://github.com/kristenchavis01/resume/commit/f8545cbb1cfdb244956345e4a1a4d098bce3c59c)). There is a new Overleaf link and we if access that link. We will get a profile photo

![overloeaf](images/overleaf.png)

Download the profile picture first and then doing bruteforce steganography on the picture that we have download earlier (In this case im using [stegseek](https://github.com/RickdeJager/stegseek))

![stegseek](images/stegseek.png)

If we open the result of stegseek, we will retrieve the flag

```
ictf{av01d_th3_z1p_b0mb_87ad2th}
```
# The Vault of Asgaard
> The flag used to fly high in the morning light, but the undead (bots) kept trying to steal it. Now we keep it in the vault of Asgaard itself! No undead fiends dare pass the test at the gates.

## About the Challenge
We have been given a website that contain a login form and a captcha

![preview](images/preview.png)

## How to Solve?
If we see a login form, the first thing that we need to test is SQL injection. So i inputted `' or true-- -` in the username but I can't click `Login` button because there is a captcha

![captcha](images/captcha.png)

To bypass the captcha, as you can see in the inspect element tab. There is a `disabled` attribute on the button. Remove that attribute so now we can login without captcha check

![bypass](images/bypass.png)

![flag](images/flag.png)

```
vikeCTF{0n1y_7h3_w0r7hy_m@y_p@55}
```
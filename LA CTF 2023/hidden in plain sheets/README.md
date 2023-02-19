# hidden in plain sheets
> I found this google sheets link on the internet. I'm sure it's hiding something, but I can't find anything? Can you find the flag?

> Choose any link (they're all the same): [Link 1](https://docs.google.com/spreadsheets/d/1OYx3lCccLKYgOvzxkRZ5-vAwCn3mOvGUvB4AdnSbcZ4/edit) [Link 2](https://docs.google.com/spreadsheets/d/17A1f0z8rmR7356fcHmHTHt3Y0JMgcHlGoflADtNXeOU/edit) [Link 3](https://docs.google.com/spreadsheets/d/1ULdm_KCOYCWuf6gqpg6tm0t-wnWySX_Bf3yUYOfZ2tw/edit)

## About the Challenge
We have been given a google sheet and we need to find the flag from that google sheet named `flag`

## How to Solve?
First we check the google sheet to find something interesting and i found new hidden sheet

![sheet](images/sheet.png)

And then in google sheet there is function named `IMPORTRANGE` to import data from another sheet even the sheet is hidden.

I immadiately create a new sheet and using the function like this
```
IMPORTRANGE("https://docs.google.com/spreadsheets/d/1OYx3lCccLKYgOvzxkRZ5-vAwCn3mOvGUvB4AdnSbcZ4", "flag!A1:AZ1")
```

And we will retrieve the flag

```
lactf{H1dd3n_&_prOt3cT3D_5h33T5_Ar3_n31th3r}
```
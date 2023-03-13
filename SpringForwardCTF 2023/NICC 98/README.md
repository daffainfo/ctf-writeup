# NICC 98
> Here’s an archive of the original NICC website from when we used to be hosted by Geocities! (Cut us some slack, it was 1998.)

> https://nicc-nicc-98.chals.io/nicc98.html

## About the Challenge
We have been given a website about NJIT Information and Cybersecurity Club

![preview](images/preview.png)

## How to Solve?
If we check on the source code there is a custom javascript file named `nicc98.js`. The content of the file is

```javascript
console.log("bmljY3tmbGlwX3RoM19zY3JpcHR9");
window.alert("Welcome to the web page of the NJIT Information and Cybersecurity Club!");
console.log("Alert successful.")
```

Decode the `bmljY3tmbGlwX3RoM19zY3JpcHR9` msg using `Base64 decoder` and you will get the flag

```
nicc{flip_th3_script}
```
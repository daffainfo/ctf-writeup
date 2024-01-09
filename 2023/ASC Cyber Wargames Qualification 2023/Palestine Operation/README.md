# Palestine Operation

> The Palestinian intelligence service was tracking an Israeli spy and terrorist who was responsible for a number of assassinations while operating undercover as “TheGhost.” They searched his apartment and discovered the attached boarding pass for the flight that he took to flee Palestine to Rome on August 1, 2023, and then our agent in Italy traced him until he traveled from Rome to Germany, specifically to Frankfurt. Your mission, if you choose to accept it, is to assist the Palestinian intelligence agency in tracing and apprehending this terrorist and revealing his secret;
He was attempting to leak a secret photo of Palestinian demonstrators in Rome. To find the photo, You must consider two approaches. The first is to trace his flight on the attached boarding pass and obtain the registration code of his aircraft. The second approach is to monitor his travel history and discover that he flew from Germany (Frankfurt) to Palestine (Tel Aviv) on February 22, 2018. Use the flight number to trace all of the flights that have occurred with this aircraft, and you will be able to determine when he will return to Palestine (Tel Aviv) from Frankfurt, as our agent reported.
After revealing these two registration codes, apply this method to combine them (1st flight registration code-2nd flight registration code) and use this combined code for your next step.

Download the image [here](images/Boarding%20Pass.jpg)

## About the Challenge

Given images which is a boarding pass from flight, so we need the aircraft registration code to complete the next step

## Solve

First we get a image like this

![boarding](images/Boarding%20Pass.jpg)

According to the description we need find the aircraft registration code on the boarding pass and at the flight history of `February 22, 2018`

On this site we manage find the [flight history](https://www.flightradar24.com/) and the aircraft registration code was `4X-EHB`

![POC 1](images/POC%201.jpg)

And the second aircraft registration code we found some site but unfortunately the registration code is wrong, but at least we already know the flight number `ELY358`

![POC 2](images/POC%202.jpg)

Because the aircraft is type `B378` so we do some bruteforce for the registration code

![POC 2](images/POC%203.jpg)

The next things is move forward after searching two aircraft registration code, in short we notice there a `QR code` and `Barcode` on the Boarding Pass image, so we scan them first

In QR code we got some link

![POC 4](images/POC%204.jpg)

And in the Barcode we got some text like password

![POC 5](images/POC%205.jpg)

When we access the link given by QR Code it's protected with password, so we do bruteforce the password, In short we found the password is according to registration code `4X-EHB-4X-EKP`

And we got the image inside

![POC 6](images/POC%206.jpg)

We download it and we do some `exiftool` and secured the interesting link

![POC 7](images/POC%207.jpg)

The pastebin is protected, and we already got password from the barcode `%@xNwvfD%4KCBPS3`

![POC 8](images/POC%208.jpg)

```
ASCWG{P4l3571N3_WiLL_B3_4LwaYs_FrE3}
```
# Catch The Scammer

> one of the well-known LEAs intercepted an encrypted message between two Russian hackers, leaking one of their competitors' ransom chat with his victim, Your mission, if you choose to accept it, is to decrypt the message, follow the ransom chat and catch the scammer, The flag will be his source fund's BTC wallet address. A quick tip: if you find yourself in need of any missing data, write an email to one of these hackers requesting the missing piece.

Download the file [here](file/Catch%20the%20Scammer_ASC.rar)

## About the Challenge

We need analyze the `.eml` file in order to know the Hacker's name and find the source BTC Address

## Solve

First we analyze the `.eml` file with [EML Analyzer](https://msgeml.com/)

So we know the sender, receiver, and body message of the email

![POC 1](images/POC%201.jpg)

According to the description we can ask the hacker to give the missing data, because the hacker was russian we change the email to `mail.ru`

![POC 2](images/POC%202.jpg)

And we found some password, so just store it

![POC 3](images/POC%203.jpg)

After some dorking we found there a twitter with username [53R3N17Y_2023](https://twitter.com/53r3n17y_2023)

And we found some interesting link

![POC 4](images/POC%204.jpg)

The inside was pgp private key to decode the pgp message

![POC 5](images/POC%205.jpg)

Because we already obtained pgp message, pgp private key, and passphrase so lets decode it

And we got some conversation inside

```
**William S**: Your computer systems have been encrypted. All your files, databases, and backups are inaccessible.

**Victim (V)**: Who is this? What's happening?

**William S**: This is not a joke. We used high-level encryption. Your IT can confirm this. We are the only ones who can provide the decryption key.

**Victim**: But why? We are a small company, we haven't harmed anyone.

**William S**: It's not personal. It's business. We have a service and you're the customer. To get your files back, you need to pay us.

**Victim**: This is illegal! I'm contacting the authorities.

**William S**: You can do so. But remember, we are the only ones who can decrypt your files. The clock is ticking.

**Victim**: I can't afford to pay you. My business is already struggling because of the pandemic.

**William S**: We could negotiate the price but remember, the more you delay, the higher the cost gets. 

**Victim**: I need to consult with my team. How do I make sure you will give the decryption key after the payment?

**William S**: Once the payment is received, we'll provide the decryption key. We have a reputation to maintain in our... industry. If we don't give the key post-payment, who would trust us in the future?

**Victim**: This is difficult. I need some time to think.

**William S**: You have 48 hours. After that, the price doubles. You know how to reach us.
```

In short, we found a site where's the all scammer database is stored [Scamsearch](https://scamsearch.io/)

According to the conversation the name of hacker is `William S**` and we do some search 

![POC 6](images/POC%206.jpg)

The only options is `William Scott`. and we got the hacker BTC Address

![POC 7](images/POC%207.jpg)

We do some address track, we got the source BTC Address

![POC 8](images/POC%208.jpg)

```
ASCWG{1A7tWftaGHohhGcJMVkkm4zAYnF53KjRnU}
```
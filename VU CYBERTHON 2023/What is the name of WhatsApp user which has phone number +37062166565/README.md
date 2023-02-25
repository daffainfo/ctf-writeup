# What is the name of WhatsApp user which has phone number +37062166565
> What is the name of WhatsApp user which has phone number +37062166565?

## About the Challenge
We need to find the name of WhatsApp user

## How to Solve?
We need to find the email by get the SQLite Database first from `/root/data/com.whatsapp/databases/wa.db`

![exports](images/exports.png)

Open the SQLite database using `DB Browser for SQlite` and import the database. In the `wa_contacts` table, we can see the email

![contacts](images/contacts.png)

```
Marcus
```
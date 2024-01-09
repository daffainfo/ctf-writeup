# We have a new contract for you

> During further investigation on the wallet that received money that we found from the transaction hash in the previous challenge, we noticed there's a token that was generated, and used to send money as part of money laundring. Could find the last address that received tokens from this contract, and the address of the smart contract?
Flag Format:ASCWG{contract address: last wallet address}

## About the Challenge

This is sequel challenge from `Track a coin from your crypto O valley of plenty`, in short we need to find the token smart contract address and the last wallet address who's has been received money

## How to Solve

In same wallet address of before challenge, you will found some suspicious smart contract address

![POC 1](images/POC%201.jpg)

You will see the name of token is `g33kso` and the smart contract address

![POC 2](images/POC%202.jpg)

And then if you click the token link you will be able to see the last transaction of the token

![POC 3](images/POC%203.jpg)

So when we wrap it to the flag format it's become

```
ASCWG{0x7b799DFbbfD91ECA3E82F2378455ab09463f1C73:0x3a79022e90fF621cd3Cc54FE95873E1A50722B97}
```
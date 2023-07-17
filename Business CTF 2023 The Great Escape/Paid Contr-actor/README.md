# Paid Contr-actor
> After a lifetime of preparation, the moment has arrived to enlist in the esteemed military of the United Nations of Zenium as an expert in blockchain security. Before embarking on your duties, there is a small matter of paperwork that requires your attention.

## About the Challenge
We have been given a zip file that contains a solidarity contract, here is the content of `Contract.sol`

```s
// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.18;


contract Contract {
    
    bool public signed;

    function signContract(uint256 signature) external {
        if (signature == 1337) {
            signed = true;
        }
    }

}
```

So, to change the value of `signed` to `true`. We need to call `signContract` using `1337` as a value

## How to Solve?
First, we need to connect to the server and get some information such as private key, address, target contract, and setup contract. And then I created another python code to call `signContract` using `1337` as a value

```python
import sys
from web3 import Web3
from solcx import compile_source, install_solc

# installs solc compiler, necessary only for first execution
install_solc("0.8.18")

# compiles source code to get the contract abi
with open("Setup.sol", "r") as fp:
    src = fp.read()
compiled = compile_source(src, output_values=["abi"])
setup_abi = compiled['<stdin>:Setup']['abi']
contract_abi = compiled['Contract.sol:Contract']['abi']

privkey = "0x29cc2c5151497caeee552c2f3480d6b2d40304ea08aeb6db591f96ee720818f7"

# blockchain gateway from tcp interface
w3 = Web3(Web3.HTTPProvider("http://94.237.62.195:34257"))
w3.eth.default_account = w3.eth.account.from_key(privkey).address
contract = w3.eth.contract(
    address="0xF6BcFF12464a2b19CFd3251eDd8F455a31F5869B", abi=setup_abi
)
print(contract.functions.__dict__)
# Get contract.sol address
contract_contract_addr = contract.functions.TARGET().call()
print("contract addr:", contract_contract_addr)
contract_contract = w3.eth.contract(
    address=contract_contract_addr, abi=contract_abi
)

# Call signContract func
res = contract_contract.functions.signContract(1337).transact()
print(res)

# check if solved()
issolved = contract.functions.isSolved().call()
print("issolved:", issolved)
```

And then check the server again to obtain the flag

![flag](images/flag.png)

```
HTB{c0n9247u14710n5_y0u_423_kn0w_p427_0f_7h3_734m}
```
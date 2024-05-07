# Readme

> this project comes from an idea of create thounds of address for many sorts of coins, and then dumps the memoric words into an veracrypt box. then we could storage the coins safely.

usage:
run the batch_gen.py to generate the address of many coins, and save it to a csv file automatically.
so that we could check the address if correct and save it to the veracrypt box.
also it delete the 10 later address in order to avoid the addr``ess be used by others.
washed.csv: deleted the mnemonic words and the private key.
result.csv: the result include the address and mnemonics of the address.


0427:
add the function of generate the address of bitcoin, and the function of generate the address of ethereum.

add the other project of generate the address offline of many addresses in order to check the address if not correct.

checked the 24 words from https://bip39.onekey.so/ and the address is same as the ETH_address output.


0428:
add BTC address and checked same to local generated address and same to bip39.onekey.so

compared imtoken,onekey wallet,trust wallet:

the ETH address is same to the local APP generated address.

imtoken & onekey wallet is same to the BIP49 address.

trust wallet is same to the BIP84 address.

0507:
add the batch generate Script to generate the address of many records.

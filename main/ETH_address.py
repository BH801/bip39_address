import os

#  一个新的生成函数
from eth_account import Account
from mnemonic import Mnemonic

# 创建一个24个词的助记词
mnemo = Mnemonic("english")
mnemonic = mnemo.generate(strength=256)  # 256位强度将生成24个词的助记词

# 使用助记词创建账户
Account.enable_unaudited_hdwallet_features()
account = Account.from_mnemonic(mnemonic)

print(account.address,'address')
print(account.key.hex(),'key hex')
print(mnemonic,'mnemonic')

if __name__ == '__main__':
    pass



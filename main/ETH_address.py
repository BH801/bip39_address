import os

#  一个新的生成函数
from eth_account import Account
from mnemonic import Mnemonic

# 创建一个24个词的助记词
mnemo = Mnemonic("english")
mnemonic = mnemo.generate(strength=256)  # 256位强度将生成24个词的助记词
mnemonic =  "catch shrimp dream peasant stumble unusual pledge pumpkin also unhappy victory slab nose athlete unknown tower grief kitchen jump actor float dog tag kid"
# 使用助记词创建账户
Account.enable_unaudited_hdwallet_features()
account = Account.from_mnemonic(mnemonic)

print(account.address,'address')
print(account.key.hex(),'key hex')
print(mnemonic,'mnemonic')



class ETH_addr():
    def __init__(self,length,memo = None,lang = 'english'):
        self.length = length
        self.mnemonic = Mnemonic(lang)
        self.memo = memo
    def generate_mnemonic(self):
        return self.mnemonic.generate(strength=256)

    def generate_address(self):
        if self.memo:
            mnemonic_words = self.memo
        else:
            mnemonic_words = self.generate_mnemonic()
        Account.enable_unaudited_hdwallet_features()
        account = Account.from_mnemonic(mnemonic_words)
        return account.address



if __name__ == '__main__':
    pass
    mnemonic_words = "catch shrimp dream peasant stumble unusual pledge pumpkin also unhappy victory slab nose athlete unknown tower grief kitchen jump actor float dog tag kid"
    eth = ETH_addr(256,memo=mnemonic_words)
    print(eth.generate_address())



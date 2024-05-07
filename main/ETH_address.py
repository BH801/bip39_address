import os

#  一个新的生成函数
from eth_account import Account
from mnemonic import Mnemonic
from config import mnemonic_words

# 创建一个24个词的助记词
# mnemo = Mnemonic("english")
# mnemonic_words = mnemo.generate(strength=256)  # 256位强度将生成24个词的助记词
# 使用助记词创建账户
Account.enable_unaudited_hdwallet_features()
account = Account.from_mnemonic(mnemonic_words)

# print(account.address,'address')
# print(account.key.hex(),'key hex')
# print(mnemonic_words,'mnemonic_words')



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
    eth = ETH_addr(256,memo=mnemonic_words)
    print(eth.generate_address())



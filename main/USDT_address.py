from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from BTC_address2BIP49 import BTC_addr49
# 24个助记词
from main.BTC_address import BTC_addr
from main.ETH_address import ETH_addr
from config import mnemonic_words


class TRON_addr():
    def __init__(self,length,memo = None,lang = 'english'):
        self.length = length
        self.mnemonic = Mnemonic(lang)
        self.memo = memo

    # 24个助记词
    def generate_address(self):
        if self.memo:
            mnemonic_words = self.memo
        else:
            mnemonic_words = self.mnemonic.generate(strength=256)
        # 生成种子
        seed_bytes = Bip39SeedGenerator(mnemonic_words).Generate()
        # 生成BIP44对象
        bip_obj_tron = Bip44.FromSeed(seed_bytes, Bip44Coins.TRON)
        # 生成私钥
        private_key_tron = bip_obj_tron.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey()
        # 生成波场地址
        tron_address = bip_obj_tron.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PublicKey().ToAddress()
        return tron_address


def USDT_addr():
    btc = BTC_addr(256,memo=mnemonic_words)
    eth = ETH_addr(256,memo=mnemonic_words)
    tron = TRON_addr(256,memo=mnemonic_words)
    return btc.generate_address(),eth.generate_address(),tron.generate_address()




"""
BTC Private Key (for Omni USDT): L53oMWsMq9RMUVxELRde4CHT3YNv7WEq98geznxWcXJWR4RWmHx7
ETH Private Key (for ERC20 USDT): 
BTC Address (for Omni USDT): 14GDhdsAphJAMHe81F8Nk8Bn6nrxyKtMLn
ETH Address (for ERC20 USDT): 0xd54dE4979E17Accb5e5383f9a507d3c235b4eb9a
TRON Private Key (for TRC20 USDT): 
TRON Address (for TRC20 USDT): TQnB3a9kpK2rtARCpGHZp6g6cnLduDBaJo
"""

if __name__ == '__main__':
    # print(USDT_addr())
    btc = BTC_addr(256,memo=mnemonic_words)
    print('btc address',btc.generate_address())
    btc49 = BTC_addr49(256,memo=mnemonic_words)
    print('btc49 address',btc49.generate_address())
    eth = ETH_addr(256,memo=mnemonic_words)
    print('eth:',eth.generate_address())
    tron = TRON_addr(256,memo=mnemonic_words)
    print('tron',tron.generate_address())
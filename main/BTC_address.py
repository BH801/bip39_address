from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

# 24个助记词
from mnemonic import Mnemonic

from config import mnemonic_words


# 生成种子
seed_bytes = Bip39SeedGenerator(mnemonic_words).Generate()

# 生成BIP44对象
bip_obj = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)

# 生成私钥
private_key = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey()

# print("Private Key:", private_key.ToWif())

# 生成比特币地址
btc_address = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PublicKey().ToAddress()

# print("BTC Address(OMNI):", btc_address)


class BTC_addr():
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
        seed_bytes = Bip39SeedGenerator(mnemonic_words).Generate()
        bip_obj = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
        private_key = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey()
        btc_address = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(
            0).PublicKey().ToAddress()
        return btc_address


if __name__ == '__main__':
    btc = BTC_addr(256,memo=mnemonic_words)
    print(btc.generate_address())



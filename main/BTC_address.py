from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

# 24个助记词
mnemonic_words = "catch shrimp dream peasant stumble unusual pledge pumpkin also unhappy victory slab nose athlete unknown tower grief kitchen jump actor float dog tag kid"

# 生成种子
seed_bytes = Bip39SeedGenerator(mnemonic_words).Generate()

# 生成BIP44对象
bip_obj = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)

# 生成私钥
private_key = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey()

print("Private Key:", private_key.ToWif())

# 生成比特币地址
btc_address = bip_obj.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PublicKey().ToAddress()

print("BTC Address:", btc_address)
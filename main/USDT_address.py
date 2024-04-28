from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

# 24个助记词
mnemonic_words = "catch shrimp dream peasant stumble unusual pledge pumpkin also unhappy victory slab nose athlete unknown tower grief kitchen jump actor float dog tag kid"

# 生成种子
seed_bytes = Bip39SeedGenerator(mnemonic_words).Generate()

# 生成BIP44对象
bip_obj_btc = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
bip_obj_eth = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)

# 生成私钥
private_key_btc = bip_obj_btc.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey()
private_key_eth = bip_obj_eth.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey()

print("BTC Private Key (for Omni USDT):", private_key_btc.ToWif())
print("ETH Private Key (for ERC20 USDT):", private_key_eth.ToWif())

# 生成比特币地址和以太坊地址
btc_address = bip_obj_btc.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PublicKey().ToAddress()
eth_address = bip_obj_eth.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PublicKey().ToAddress()

print("BTC Address (for Omni USDT):", btc_address)
print("ETH Address (for ERC20 USDT):", eth_address)





from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

# 24个助记词
mnemonic_words = "catch shrimp dream peasant stumble unusual pledge pumpkin also unhappy victory slab nose athlete unknown tower grief kitchen jump actor float dog tag kid"

# 生成种子
seed_bytes = Bip39SeedGenerator(mnemonic_words).Generate()

# 生成BIP44对象
bip_obj_tron = Bip44.FromSeed(seed_bytes, Bip44Coins.TRON)

# 生成私钥
private_key_tron = bip_obj_tron.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PrivateKey()

print("TRON Private Key (for TRC20 USDT):", private_key_tron.ToWif())

# 生成波场地址
tron_address = bip_obj_tron.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0).PublicKey().ToAddress()

print("TRON Address (for TRC20 USDT):", tron_address)


"""
BTC Private Key (for Omni USDT): L53oMWsMq9RMUVxELRde4CHT3YNv7WEq98geznxWcXJWR4RWmHx7
ETH Private Key (for ERC20 USDT): 
BTC Address (for Omni USDT): 14GDhdsAphJAMHe81F8Nk8Bn6nrxyKtMLn
ETH Address (for ERC20 USDT): 0xd54dE4979E17Accb5e5383f9a507d3c235b4eb9a
TRON Private Key (for TRC20 USDT): 
TRON Address (for TRC20 USDT): TQnB3a9kpK2rtARCpGHZp6g6cnLduDBaJo
"""
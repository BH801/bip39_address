from BTC_address import BTC_addr
from ETH_address import ETH_addr
from USDT_address import USDT_addr, TRON_addr
from main.BTC_address2BIP49 import BTC_addr49
import pandas as pd

from mnemonic import Mnemonic
# if __name__ == '__main__':
#     print('888')
#     pass
def batch_gen():
    path = "K:/result.csv"
    num = 30000
    with open(path,'w+',encoding='utf-8') as f:
        f.write(','.join(['btc_addrBIP44','btc49_addr','eth_addr','trc20_addr','mnemonic'])+'\n')
        for i in range(num):
            print(i)
            mnemonic = Mnemonic('english')
            mnemonic_words = mnemonic.generate(strength=256)
            btc = BTC_addr(256,memo=mnemonic_words)
            eth = ETH_addr(256,memo=mnemonic_words)
            trc20 = TRON_addr(256,memo=mnemonic_words)
            btc49 = BTC_addr49(256,memo=mnemonic_words)
            f.write(','.join([btc.generate_address(),btc49.generate_address(),eth.generate_address(),trc20.generate_address(),mnemonic_words])+'\n')
    df = pd.read_csv(path)
    # del the 10 line after of the mnemonic column
    df.loc[10:,'mnemonic'] = None
    df.to_csv('K:/washed.csv')

if __name__ == '__main__':
    batch_gen()
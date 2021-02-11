# PythonCryptoCurrencyPriceChecker

This code uses Python Binance module to check the prices and 24h percentchange for three crypto currencies - BTC, XRP, and DOGE.
You will need to create an account on Binance and have your own api_key and api_secret.

To use this code, simply run the file binan.py from command line. Just make sure to run it from the same directory the file is in.
(I recommend creating a folder and putting all the pictures and python file in the folder.)


Sample: 

    C:\Users\PATH\PATH\PATH>python binan.py
    
You can also add new coins. To do this:
  1. You will have to have the pricture of the currency and put it in the same folder along with binan.py.
  2. You will have to make two changes in binan.py:
  At the layout section, you will need to add sg.Tab("CoinName", tabs("CoinName"), border_width="18"). *Coinname has to be capitalized.*
  In the end of the code, there is a list called "a_list". You will need to append the coinname to the list, too.
  
  This is an ongoing project. I will add more features in the future.

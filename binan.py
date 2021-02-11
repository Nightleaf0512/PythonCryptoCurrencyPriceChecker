from binance.client import Client
import PySimpleGUI as sg

api_key = "your_binance_apikey"
secret_key = "your_binance_secretkey"
client = Client(api_key=api_key, api_secret=secret_key)

# price
def get_price(coin):
    return round(float(client.get_symbol_ticker(symbol=f"{coin}USDT")['price']), 5)

def column_layout_price(coin):
    col =[[sg.Text(f"{get_price(coin)}", font=("Arial", 9, 'bold'), size=(10,1), pad=(15,10), key=coin)]]
    return col

# 24h percentchange
def price_change_24h(coin):
    return round(float(client.get_ticker(symbol=f"{coin}USDT")["priceChangePercent"]), 2)    

def column_layout_change(coin):
    if price_change_24h(coin) == 0:
        return [[sg.Text(f"{price_change_24h(coin)}%", font=("Arial", 9, 'bold'), size=(7,1), pad=(40,10), text_color="black", key=f"{coin}change")]]
    elif price_change_24h(coin) > 0:
        return [[sg.Text(f"+{price_change_24h(coin)}%", font=("Arial", 9, 'bold'), size=(7,1), pad=(40,10), text_color="green", key=f"{coin}change")]] 
    return [[sg.Text(f"{price_change_24h(coin)}%", font=("Arial", 9, 'bold'), size=(7,1), pad=(40,10), text_color="red", key=f"{coin}change")]]

def update_24h_change(coin):
    if price_change_24h(coin) == 0:
        window[f"{coin}change"].update(f"+{price_change_24h(coin)}%", text_color="black")
    elif price_change_24h(coin) > 0:
        window[f"{coin}change"].update(f"+{price_change_24h(coin)}%", text_color="green")
    elif price_change_24h(coin) < 0:
        window[f"{coin}change"].update(f"{price_change_24h(coin)}%", text_color="red")

# GUI
sg.theme('DefaultNoMoreNagging')

# Tabs
def tabs(coin): 
    tab_layout = [[sg.Image("{}.png".format(coin), size=(50,50)),
                   sg.Text("Price", font=("Arial", 10, 'bold'), size=(7,1), pad=(40,40)), sg.Text("24h change", font=("Arial", 10, 'bold'), size=(10,1), pad=(10,40))],
                  [sg.Text(f"{coin}/USDT", font=("Arial", 9, 'bold')), sg.Column(column_layout_price(coin)), sg.Column(column_layout_change(coin))]]
    return tab_layout

# Layout
layout = [[sg.Text("Crypto Currencies", font=("Arial", 10, 'bold'))],
          [sg.TabGroup([[sg.Tab("BTC", tabs("BTC"), border_width="18"), sg.Tab("XRP", tabs("XRP"), border_width="18"), sg.Tab("DOGE", tabs("DOGE"), border_width="18")]])]]

window = sg.Window("NightLeaf Crypto", layout)

def coin_window(*coins):
    for coin in coins:
        globals()[f"{coin}_last_price"] = 1
        
    while True:
        event,values = window.read(timeout=600)
        if event == sg.WIN_CLOSED:
            break 

        for coin in coins:
            update_24h_change(coin)
            price = get_price(coin)
            
            if price != globals()[f"{coin}_last_price"]:
                if price > globals()[f"{coin}_last_price"]:
                    window[f"{coin}"].update(f"{price} 🠕", text_color="green")              
                elif price < globals()[f"{coin}_last_price"]:
                    window[f"{coin}"].update(f"{price} 🠗", text_color="red")
                globals()[f"{coin}_last_price"] = price


a_list =["BTC", "XRP", "DOGE"]
coin_window(*a_list)
    

import requests
import random
import sys

from requests.api import request

##API Information
_ENDPOINT = "https://api.binance.com"
COINMARKET_API_KEY = "ea442960-9bcf-4d5b-8887-c907d4210123"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
}

coins_list = []

data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
    coins_list.append(cripto["symbol"])

##General Variables
coins = tuple(coins_list)
amount = ""
total = 0
id_code = random.randrange(999)
file = open("history.csv", "a")

##Validation Functions    
def _url(api):
    return _ENDPOINT + api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+ cripto))

def iscoin(cripto):
    return cripto in coins

##Exit Prgram Option
def exit_program():
    alert = input("Press 'c' to close the app\n : ")
    response = ""
    if response == "c" or "close":
        print("Closing Program")
        sys.exit(0)
        
##Transactions History
def show_history():
    print("History")
    file = open("history.csv")
    print (file.read())
    file.close()
        
##Currencies Prices
def check_price():
    coin = input("Enter the currency\n: ")
    while not iscoin(coin):
     print("Invalyd currency")
     coin = input("Enter the currency\n: ")
    else:
     data = get_price(coin + "USDT").json()
     print("El precio es USD de ",coin,"es",data,["price"]) 
     
##Get Currency Function
def get(total, amount, id_code):
    coin = input("Select the currency that you want to get\n: ")
    cotiz = ""
    code = id_code

    while not iscoin(coin):
        print("Invalyd currency")
        coin = input("Enter the currency that you want to get\n: ")
    else:
         print("The currency " + coin + " is valyd")
         print("Your code is\n ", code)

    if code == id_code:
        code = input("Please enter the code here to continue\n: ")
    else:
        print("Invalyd code.")
        code = input("Please enter the code here to continue\n: ")

    while not cotiz.replace('.','',1).isdigit():
        cotiz = input("Enter the cotization in USD for "+ coin +"\n : ")

          
    while not amount.replace('.','',1).isdigit():
        amount = input("Enter the desired amount of "+ coin + " : ")
        if amount > "0":
            current_balance = total + float(amount) * float(cotiz)
            print("You received "+ amount +" USD of "+ coin)
            print("Your Current Balance is: "+ str(current_balance) +" USD")
            file.write("Currency Received: ")
            file.write(coin)
            file.write(", ")
            file.write("Amount: ")
            file.write(amount)
            file.write("USD")
            file.write(", ")
            file.write("Cotization: ")
            file.write(cotiz)
            file.write(", ")
            file.write("Balance: ")
            file.write(str(current_balance))
            file.write("\n")
            file.close()
        elif amount <= "0":
            print("There's no Balance in your Wallet.")
            
##Send Function
def send(total, amount, id_code):
    coin = input("Select the currency that you will send\n: ")
    code = id_code
    cotiz = ""
    total = random.randrange(100000)
    while not iscoin(coin):
        print("Invalyd currency")
        coin = input("Select the currency that you will send\n: ")
        break
    else:
        print("The currency selected is Valyd")
    if code == id_code:
        print(code," Use this code to continue with the transaction...\n")
        code = input("Enter the code please\n: ")
    elif code != id_code:
        print("Code does not match")
        code = input("Please enter the correct code\n: ")
    else:
        print("Code accepted!")
    while not cotiz.replace('.','',1).isdigit():
        cotiz = input("Enter the cotization in USD for "+ coin +" : ")
        break
    else:
        print("Invalyd number")
        cotiz = input("Enter the cotization in USD for "+ coin +" : ")
    while not amount.replace('.','',1).isdigit():
        amount = input("Enter the amount that's going to be sent: ")
        break
    else:
        print("Invalyd amount")
        amount = input("Enter the amount that's going to be sent: ")
    if amount > "0":
        current_balance = total - float(amount) * float(cotiz)
        print("You've sent "+amount+" USD of "+coin)
        print("Your Current Balance is "+str(current_balance)+" USD")
        file.write("Currency Sent: ")
        file.write(coin)
        file.write(", ")
        file.write("Amount: ")
        file.write(amount)
        file.write("USD")
        file.write(", ")
        file.write("Cotization: ")
        file.write(cotiz)
        file.write(", ")
        file.write("Balance: ")
        file.write(str(current_balance))
        file.write("\n")
        file.close()
    elif amount <= "0":
        print("No Balance available in your Wallet")
        
##Program Menu         
message = input("Menu:\n Select option:\n - get(currency)\n - send(currency)\n - check(price)\n - View Transaction History\n - exit\n: ")

if message.casefold() == "get" :
    get(total, amount, id_code)     
elif message.casefold() == "send" :
    send(total, amount, id_code)
elif message.casefold() == "check" :
    check_price()
elif message.casefold() == "history":
    show_history()
elif message.casefold() == 'exit':
    exit_program()    
else:
    print("Please Select a Valyd Option.")

            
 
     
    

     
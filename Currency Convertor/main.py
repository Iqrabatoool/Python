import requests
import json
api_key = "https://api.currencyapi.com/v3/latest?apikey=cur_live_jDwzHHaD9cKEfXLvjW9IPmlhOojU4E3vxnunogTK"
data = requests.get(api_key).text
data1 = json.loads(data)
loop = 1
while loop ==1:

    check = int(input("Press 1 to get all Currency Codes | Press 2 to convert your amount | 3 to quit : "))

    def conversion():
        amount = float(input("Enter the amount you want to convert : "))
        From = input("From : ").upper()
        To =input("To : ").upper()
        Fromcurrency = data1["data"][From]['value']
        Tocurrency = data1["data"][To]['value']
        Total = round(amount * Tocurrency / Fromcurrency, 4)
        print(Total)

    def display():
        Code = data1["data"]
        for i in Code:
            print(f' Currency Code =  {i} ')
        
    if check == 1:
        display()
    elif check ==2:
        conversion()
    else:
        print("Program will terminate now")
        loop = 0

    loop = int(input("Press 1 to rerun this program or Press 0 to Quit : "))
    



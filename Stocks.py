import requests
from bs4 import BeautifulSoup
import datetime
import pandas
import msvcrt as m

#Function to request the website and parse for the required information
def price(websites, list):
    page = requests.get(websites)
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    name = soup.find("h1").contents
    price = soup.find("div", {"class" : "pcnsb div_live_price_wrap"}).span.contents
    list.append(float(price[0]))

def wait():
    m.getch()

#Websites
websites = ["https://www.moneycontrol.com/india/stockpricequote/constructioncontracting-real-estate/dlf/D04",
            "https://www.moneycontrol.com/india/stockpricequote/steel-large/tatasteel/TIS",
            "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI",
            "https://www.moneycontrol.com/india/stockpricequote/telecommunications-service/vodafoneidealimited/IC8",
            "https://www.moneycontrol.com/india/stockpricequote/misc-commercial-services/irctc-indianrailwaycateringtourismcorp/IRC",
            "https://www.moneycontrol.com/india/stockpricequote/telecommunications-service/bhartiairtel/BA08",
            "https://www.moneycontrol.com/india/stockpricequote/constructioncontracting-real-estate/embassyofficeparksreit/EOP",
            "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/yesbank/YB"]
dict = {}
today = datetime.datetime.today()

#Lists
Date = []
DLF = []
Tata_Steel = []
RIL = []
VodaIdea= []
IRCTC = []
Airtel = []
Embassy = []
Yes = []

#Dictionaries
dict["Date"] = Date
dict["DLF Ltd."] = DLF
dict["Tata Steel Ltd."] = Tata_Steel
dict["Reliance Industries Ltd."]  = RIL 
dict["Vodafone Idea Ltd."] = VodaIdea
dict["IRCTC"] = IRCTC
dict["Bharti Airtel Ltd."] = Airtel
dict["Embassy Office Parks REIT Ltd."] = Embassy
dict["Yes Bank Ltd."] = Yes

#Adding Data
Date.append(today)
print("DLF")
price(websites[0], DLF)
print(DLF)
print("TATA STEEL")
price(websites[1],Tata_Steel)
print(Tata_Steel)
print("RIL")
price(websites[2], RIL)
print(RIL)
print("VODA IDEA")
price(websites[3], VodaIdea)
print(VodaIdea)
print("IRCTC")
price(websites[4], IRCTC)
print(IRCTC)
print("AIRTEL")
price(websites[5], Airtel)
print(Airtel)
print("EMBASSY")
price(websites[6], Embassy)
print(Embassy)
print("YES")
price(websites[7], Yes)
print(Yes)

#print(dict)
df = pandas.DataFrame(dict)
df.to_csv("E:\Code\Python\WebScapper\Stock_Tracker.csv", mode="a", header=False)
print(df)
print("Press Enter to Exit")
wait()

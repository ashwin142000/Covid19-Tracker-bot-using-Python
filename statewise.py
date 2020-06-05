from bs4 import BeautifulSoup
import requests
import pandas as pd
url="https://www.mohfw.gov.in/"
def get_data(url):
 data = requests.get(url)
 return data

def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data=get_data(url)
    bs = BeautifulSoup(html_data.text,'html.parser')
    print()
    print("Covid19 India Report")
    print()
    infodiv =bs.find("li", class_ = "bg-blue")
    print("Active cases : ",infodiv.strong.text)
    infodiv2 = bs.find("li",class_ = "bg-green")
    print("Discharged : ", infodiv2.strong.text)
    infodiv3 = bs.find("li",class_ = "bg-red")
    print("Deaths : ", infodiv3.strong.text)
    infodiv4 = bs.find("li",class_ = "bg-orange")
    print("Migrated : ", infodiv4.strong.text)
    print()
    
get_corona_detail_of_india()

d=pd.read_html(url,header=0)
pd.options.display.width=None


df=d[0]
df.drop(df.tail(4).index,inplace=True)
state=input("Enter a State name to get latest Covid19 updates about that State:")

statewise=df.loc[df['Name of State / UT']==state.title()]
print(statewise)
a=input("Do you want to see every States Covid19 Updates? [y/n]")
if a=='y':
	print(df)
else: 
	b = input("Enter any key to exit")    
    



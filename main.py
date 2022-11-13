import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.flipkart.com/search?q=gaming+laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_sc_na_na&as-pos=1&as-type=RECENT&suggestionId=gaming+laptop%7CLaptops&requestId=888d9fd0-86d8-4b89-96cb-e6fd7ced053b&as-searchtext=gaminlaptops"

#Phrase content into HTML
req = requests.get(url)
content = BeautifulSoup(req.content,'html.parser')

data=content.find_all('div',{'class':'_2kHMtA'})

links=[]
product_name=[]
product_price=[]
start_link="https://www.flipkart.com"

for item in data:
    rest_link=item.find('a')['href']
    name=item.find('div',attrs={'class':'_4rR01T'})
    price=item.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    product_name.append(name.text)
    product_price.append(price.text)
    links.append(start_link+rest_link)


initial_dataframe={'Product_name':product_name,'Product_price':product_price,'Link':links}
final_dataframe=pd.DataFrame(initial_dataframe)

print(final_dataframe)
final_dataframe.to_csv('data.csv')
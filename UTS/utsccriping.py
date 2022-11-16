import requests
from bs4 import BeautifulSoup
import pandas as pd

array_addr=[]
def addr_url(addr):
    addr={}
    addr["addr_gambar"] = i.find("img")
    addr["addr_harga"] = i.find("p",class_="price_color").text
    addr["addr_judul"] = i.find("h3").text
    addr["addr_rate"] = i.find("p", class_="star-rating")
    array_addr.append(addr)
    return array_addr

def rubah_rating(rate):
    if rate =="One":
        jml_rate = "1"
    elif rate =="Two":
        jml_rate = "2"
    elif rate =="Three":
        jml_rate = "3"
    elif rate =="Four":
        jml_rate = "4"
    elif rate =="Five":
        jml_rate = "5"
    return jml_rate 

try:
    data =[]
    for page in range(1,2):
        html = requests.get('https://books.toscrape.com/catalogue/page-'+str(page)+'.html')
        html_soup = BeautifulSoup(html.content, "html.parser")
        all_author = html_soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for i in all_author:
            addr_url(i)

            for x in array_addr:
                gambar = x["addr_gambar"]['src']
                judul = x["addr_judul"]
                harga = x["addr_harga"].replace("£","")
                rating = rubah_rating(x["addr_rate"]["class"][1])            
            data.append({
                'gambar' :gambar,
                'judul' : judul,
                'harga' :harga,
                "rating" : rating
            })

    df = pd.DataFrame (data)
    df.to_csv('data_book.csv', encoding='utf-8')
    print('Selesai Menyimpan data csv.....')
except Exception as err: 
    print(f"Teajadi kesalahan : {err}")
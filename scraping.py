from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas
import time

# option untuk selenium
opsi = webdriver.ChromeOptions()
opsi.add_argument('--headless')

# service (cromedirver)
file = Service('chromedriver.exe')

# Link Web (LAZADA)
link = "https://www.lazada.co.id/catalog/?q=redmi+11+pro&_keyori=ss&from=input&spm=a2o4j.searchlistbrand.search.go.537349d7IWf6PC"

# setting driver
driver = webdriver.Chrome(service=file, options=opsi)
driver.set_window_size(1300, 800)
driver.get(link)

# jeda
time.sleep(5)

# Ambil gambar
driver.save_screenshot("coba.png")

content = driver.page_source

driver.quit()

data = BeautifulSoup(content, 'html.parser')


list_nama = []
list_gambar = []
list_harga = []
list_kota = []
list_link = []

i =1


for item in data.find_all('div', class_="qmXQo"):
    print(i)
    
    nama = item.find('div', class_="RfADt").find('a').get_text()
    link = item.find('div', class_="RfADt").find('a')['href']
    gambar = item.find('img', class_="jBwCF")['src']
    harga = item.find('span', class_="ooOxS").get_text()
    kota = item.find('span', class_="oa6ri").get_text()
    
    list_nama.append(nama)
    list_link.append(link)
    list_harga.append(harga)
    list_kota.append(kota)
    list_gambar.append(gambar)

    i+=1

# Data Frame
df = pandas.DataFrame({
    'Nama' : list_nama,
    'Harga' : list_harga,
    'Kota' : list_kota,
    'Link' : list_link,
    'Gambar' : list_gambar,
    })

# Membuat File Excel
writer = pandas.ExcelWriter('xiaomi.xlsx')
df.to_excel(writer, sheet_name='Sheet1', index = False)
writer.save()
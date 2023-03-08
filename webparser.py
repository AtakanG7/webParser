from bs4 import BeautifulSoup  
import requests
import csv 
import pandas as pd

url  = "https://www.amazon.com.tr/deal/6ef7f2d8/?_encoding=UTF8&_ref=dlx_gate_dd_dcl_tlt_6ef7f2d8_dt&pd_rd_w=LO8YX&content-id=amzn1.sym.acc759a7-46b5-4357-a838-e1ff805de00b&pf_rd_p=acc759a7-46b5-4357-a838-e1ff805de00b&pf_rd_r=46NKPX8HJ8QWZMC44C43&pd_rd_wg=ntJCV&pd_rd_r=26f20799-1b4f-4037-a43c-8ac5e2d4f0fc&ref_=pd_gw_unk"

#find the requested page!
response = requests.get(url)

#get its content
response = response.content

#parse the data into html!
html = BeautifulSoup(response , "html.parser")

#parsing...
li = html.find_all("li", class_="octopus-response-li-width")

#shaping the data...
with open("file.csv", "w" , encoding='utf-8') as f:
    for line in li:

        #reaching the exact data!
         image = line.find("img")
         title = image.attrs['alt']
         prices = line.find("span", class_="a-offscreen").text

         #writing data into csv file...
         writer = csv.writer(f)
         writer.writerow([title ,prices])
         

    



   
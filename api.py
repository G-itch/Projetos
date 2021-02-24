import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com.br/L%C3%A2mpada-Xiaomi-Colorida-Inteligente-Original/dp/B07CXMQY45/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=328BNEL2XIY1H&dchild=1&keywords=yeelight&qid=1590933393&sprefix=yee%2Caps%2C378&sr=8-1"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

page = requests.get(URL,headers=header)

soup = BeautifulSoup(page.content, "html.parser")
title = soup.find(id="productTitle").get_text()

print(title.strip())
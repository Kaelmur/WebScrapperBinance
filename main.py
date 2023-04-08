from bs4 import BeautifulSoup
import requests


URL = "https://www.binance.com/en/markets/overview"

response = requests.get(URL)

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
coin = soup.find_all(name="div", class_="css-vlibs4")
for i in coin:
    name = i.a.getText()[:3]
    price = i.find(name="div", class_="css-ydcgk2").getText()
    percentage = i.find(name="div", class_="css-18yakpx").getText()
    volume = i.find(name="div", class_="css-102bt5g").getText()
    capitalization = i.find(name="div", class_="css-s779xv").getText()
    link = f'https://www.binance.com{i.find("a").get("href")}'
    with open("coins.csv", "a") as f:
        f.write(f"{name} | {price} | {percentage} | {volume} | {capitalization} | {link}\n")

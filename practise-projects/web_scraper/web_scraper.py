import requests
from bs4 import BeautifulSoup
import pandas as pd
# Web Scraper Project
# Scrapes quotes, author names, tags, and heading from quotes.toscrape.com
# Learned: requests, BeautifulSoup, pandas


url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

heading = soup.find('h1').text.strip()
print(heading)
master_list = []
quote_box = soup.find_all("div", class_="quote")
for box in quote_box:
    text = box.find("span", class_="text").text
    author = box.find("small", class_="author").text
    tag_list = box.find_all("a", class_="tag")
    tags= ", ".join(tag.text.strip() for tag in tag_list)
    master_list.append({ 'Heading':heading,'Quotes':text,'Author':author, 'Tags':tags} )

df =pd.DataFrame(master_list)

df.to_csv('report.csv', index=False, encoding="utf-8-sig")

print("Scraping complete! CSV saved as 'report.csv'.")
    
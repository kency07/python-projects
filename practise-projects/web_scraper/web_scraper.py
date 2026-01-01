import requests
from bs4 import BeautifulSoup
import csv
# Web Scraper Project
# Scrapes quotes, tags, and heading from quotes.toscrape.com
# Learned: requests, BeautifulSoup, file writing


url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

heading = soup.find('h1')
print(heading.text.strip())
tags = soup.find_all("span", class_="tag-item")
for tag in tags:
    print(tag.text.strip())
quotes = soup.find_all("span", class_ = "text")

for quote in quotes:
    print(quote.text.strip())
with open ("scraper.txt", "w", encoding="utf-8") as file:
    file.write(f"heading:\n{heading.text.strip()}\n")
    file.write("Tags:" "\n")
    for tag in tags:
        file.write(f"{tag.text.strip()}\n")
    file.write("Quotes:" "\n")    
    for quote in quotes:
        file.write(f"{quote.text.strip()}\n")
    
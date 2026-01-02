import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Web Scraper Project
# Scrapes quotes, author names, tags, and heading from quotes.toscrape.com
# Learned: requests, BeautifulSoup, pandas, pagination, handle request failures and timeouts


base_url = "https://quotes.toscrape.com"
master_list = []
current_page = "/page/1/"
heading = None
scraping_successful = False
while current_page:
    url = base_url + current_page
    print(f"Scraping: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        scraping_successful = True

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    if heading is None:
        heading = soup.find("h1").text.strip()
    quote_boxes = soup.find_all("div", class_="quote")
    for box in quote_boxes:
        text = box.find("span", class_="text").text.strip()
        author = box.find("small", class_="author").text.strip()
        tag_list = box.find_all("a", class_="tag")
        tags = ", ".join(tag.text.strip() for tag in tag_list)
        master_list.append(
            {"Heading": heading, "Quotes": text, "Author": author, "Tags": tags}
        )
    next_btn = soup.find("li", class_="next")
    if next_btn:
        current_page = next_btn.find("a")["href"]
        time.sleep(1)
    else:
        current_page = None
if scraping_successful and master_list:
    df = pd.DataFrame(master_list)

    # df.to_csv('report.csv', index=False, encoding="utf-8-sig")

    print("Scraping complete! CSV saved as 'report.csv'.")
else:
    print("Scraping failed. No CSV file was created.")

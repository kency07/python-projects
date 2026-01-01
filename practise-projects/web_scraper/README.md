# Web Scraper Project (Python)

This is a beginner web scraping project using Python.
It scrapes quotes, authors, tags, and the page heading from quotes.toscrape.com
 and saves the data into a CSV file.
___

## What it does
- Scrapes the page heading (`<h1>`)

- Scrapes quotes (`<span class="text">`)

- Scrapes author names (`<small class="author">`)

-Scrapes all tags for each quote (`<a class="tag">`)

- Saves the data to a CSV file (report.csv) using UTF-8 encoding for Excel compatibility
___

## Technologies Used
- Python

- requests – for sending HTTP requests

- BeautifulSoup (bs4) – for parsing HTML

- pandas – for storing data and exporting to CSV
___

## Website Scraped
https://quotes.toscrape.com
___

## Output
- The script generates a CSV file containing the following columns:

- Heading – the page heading (optional)

- Quotes – the text of the quote

- Author – the name of the author

- Tags – all tags for the quote, joined by commas
___

## Output Example

| Heading         | Quotes                                                                                             | Author            | Tags                        |
|-----------------|---------------------------------------------------------------------------------------------------|-----------------|----------------------------|
| Quotes to Scrape | “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.” | Albert Einstein | change, thinking, process  |
| Quotes to Scrape | “It is our choices, Harry, that show what we truly are, far more than our abilities.”             | J.K. Rowling     | choices, abilities          |

---
## What I Learned

- How to send HTTP requests using Python

- How to parse HTML with BeautifulSoup

- How to extract elements by class and tag

- How to store scraped data in a CSV file with pandas

- How to handle multiple tags per quote
___

## Future Improvements

- Add error handling for failed HTTP requests
- Scrape multiple pages (pagination)
- Include additional metadata if available (e.g., quote IDs or author info)
- Make CSV output optional or customizable
# Web Scraper Project (Python)

This is a beginner-friendly web scraping project built with Python.
It scrapes quotes, authors, tags, and the page heading from
[quotes.toscrape.com](https://quotes.toscrape.com) and saves the data into a CSV file.

---

## What It Does
- Scrapes the page heading (`<h1>`)
- Scrapes quotes (`<span class="text">`)
- Scrapes author names (`<small class="author">`)
- Scrapes all tags for each quote (`<a class="tag">`)
- Automatically navigates through multiple pages (pagination)
- Handles HTTP request errors gracefully
- Saves the data to a CSV file (`report.csv`) using UTF-8 encoding for Excel compatibility

---

## Technologies Used
- Python
- `requests` – for sending HTTP requests
- `BeautifulSoup` (bs4) – for parsing HTML
- `pandas` – for storing data and exporting to CSV
- `time.sleep()` - Add a delay helps ensure the server doesn't crash from too many requests 
---

## Website Scraped
https://quotes.toscrape.com

---

## Output
The script generates a CSV file containing the following columns:

- **Heading** – the page heading
- **Quotes** – the text of the quote
- **Author** – the name of the author
- **Tags** – all tags associated with the quote, joined by commas

---

## Output Example

| Heading          | Quotes                                                                                             | Author            | Tags                       |
|------------------|---------------------------------------------------------------------------------------------------|------------------|----------------------------|
| Quotes to Scrape | “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.” | Albert Einstein | change, thinking, process |
| Quotes to Scrape | “It is our choices, Harry, that show what we truly are, far more than our abilities.”             | J.K. Rowling     | choices, abilities         |

---

## What I Learned
- How to send HTTP requests using Python
- How to handle request failures and timeouts
- How to parse HTML with BeautifulSoup
- How to extract multiple elements from a page
- How to scrape paginated websites
- How to store structured data using pandas

---

## Future Improvements
- Add retry logic for failed requests
- Add logging instead of print statements
- Allow configurable output filenames
- Scrape additional metadata (e.g., author profile pages)

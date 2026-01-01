# Web Scraper Project (Python)

This is a beginner web scraping project using Python.
___

## What it does
- Scrapes the page heading (h1)
- Scrapes tags(tag-items)
- Scrapes quotes
- Saves data to a text file
___

## Technologies Used
- Python
- requests
- BeautifulSoup
___

## Website Scraped
https://quotes.toscrape.com
___

## Output
The script generates a text file containing scraped data.
___

## Output Example

The `scraper.txt` file will look something like this:
```
heading:
Quotes to Scrape
Tags:
love
inspirational
life
Quotes:
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
“It is our choices, Harry, that show what we truly are, far more than our abilities.”

```
---
## What I Learned
- How to send HTTP requests
- How to parse HTML
- How to extract elements without classes
- How to save scraped data to a file
___

## Future Improvements

- Add error handling for failed HTTP requests
- Scrape multiple pages (pagination)
- Store data in a csv file
- Extract additional information (author names)
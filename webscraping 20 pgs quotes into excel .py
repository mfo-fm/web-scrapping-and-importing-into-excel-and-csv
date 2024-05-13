import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'http://quotes.toscrape.com/'
page_number = 1
max_pages = 20  # Maximum number of pages to scrape
quotes_per_page = 10  # Number of quotes per page

all_quotes = []

while page_number <= max_pages:
    url = f'{base_url}page/{page_number}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        if quotes:
            for quote in quotes:
                text = quote.find('span', class_='text').text.strip()
                author = quote.find('small', class_='author').text.strip()
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                all_quotes.append({'Quote': text, 'Author': author, 'Tags': ', '.join(tags)})
        
        page_number += 1
    else:
        print(f'Failed to retrieve data from {url}.')
        break

if all_quotes:
    df = pd.DataFrame(all_quotes)
    df.to_excel('quotes.xlsx', index=False)
    print("Quotes exported to quotes.xlsx successfully.")
else:
    print("No quotes found.")

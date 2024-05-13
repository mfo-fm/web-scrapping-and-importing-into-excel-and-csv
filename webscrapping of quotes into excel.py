import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://quotes.toscrape.com/' 

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if quotes:
        data = []
        for quote in quotes:
            text = quote.find('span', class_='text').text.strip()
            author = quote.find('small', class_='author').text.strip()
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            data.append({'Quote': text, 'Author': author, 'Tags': ', '.join(tags)})

        df = pd.DataFrame(data)
        df.to_excel('quotes.xlsx', index=False)
        
        print("Quotes exported to quotes.xlsx successfully.")
    else:
        print("No quotes found.")
else:
    print('Failed to retrieve data from quotes.toscrape.com.')
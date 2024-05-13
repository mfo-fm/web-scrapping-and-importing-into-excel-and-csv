import requests
from bs4 import BeautifulSoup
import csv

url = 'http://quotes.toscrape.com/' 

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    if quotes:
        with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Quote', 'Author', 'Tags']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for quote in quotes:
                text = quote.find('span', class_='text').text.strip()
                author = quote.find('small', class_='author').text.strip()
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                
                writer.writerow({'Quote': text, 'Author': author, 'Tags': ', '.join(tags)})
                
        print("Quotes exported to quotes.csv successfully.")
    else:
        print("No quotes found.")
else:
    print('Failed to retrieve data from quotes.toscrape.com.')
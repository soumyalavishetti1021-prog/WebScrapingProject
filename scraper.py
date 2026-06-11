import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    print("QUOTES FROM WEBSITE")
    print("-" * 50)

    for i in range(len(quotes)):
        print(f"\nQuote {i+1}")
        print(quotes[i].text)
        print("Author:", authors[i].text)

else:
    print("Failed to fetch data")
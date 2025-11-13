import requests
from bs4 import BeautifulSoup

def get_quotes():
    response = requests.get("http://quotes.toscrape.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = [quote.text for quote in soup.select(".text")]
    return quotes
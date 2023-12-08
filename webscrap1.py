import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        print(soup.get_text)

        print(soup.prettify)

        # Extract book titles and prices
        book_titles = [h3.a['title'] for h3 in soup.find_all('h3')]
        prices = [p.text for p in soup.select('p.price_color')]

        # Display the results
        for title, price in zip(book_titles, prices):
            print(f"Title: {title}\nPrice: {price}\n")

if __name__ == "__main__":
    books_url = 'https://books.toscrape.com/'
    scrape_books(books_url)

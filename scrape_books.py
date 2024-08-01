import aiohttp
from bs4 import BeautifulSoup
from manage import db
from model import Books

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_books():
    books = []
    page = 1
    async with aiohttp.ClientSession() as session:
        while True:
            url = f"http://books.toscrape.com/catalogue/page-{page}.html"
            html = await fetch(session, url)
            soup = BeautifulSoup(html, 'html.parser')
            
            book_divs = soup.find_all('article', class_='product_pod')
            if not book_divs:
                break
            
            for book in book_divs:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').get_text()
                availability = book.find('p', class_='instock availability').get_text(strip=True)
                books.append({"title": title, "price": price, "availability": availability})
            page += 1
    return books


def save_to_db(books):
    for book in books:
        new_book = Books(
            title=book['title'],
            price=book['price'],
            availability=book['availability'],
        )
        db.session.add(new_book)
    db.session.commit()

import asyncio
from flask import Flask, render_template, jsonify
from manage import db, init_app
from model import Books
from scrape_books import scrape_books, save_to_db

app = Flask(__name__)
init_app(app)

@app.route('/')
def index():
    books = Books.query.all()
    return render_template('index.html', books=books)

@app.route('/api/books', methods=['GET'])
def api_books():
    books = Books.query.all()
    return jsonify([{
        'id': book.id,
        'title': book.title,
        'price': book.price,
        'availability': book.availability,
        'image_url': book.image_url
    } for book in books])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    books = loop.run_until_complete(scrape_books())
    with app.app_context():
        save_to_db(books)
    print(f"Scraped {len(books)} books and saved to books.db")
    app.run(debug=True)

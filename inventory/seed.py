import random
from inventory.models import Publisher, Author, Genre, Book, Store, Inventory


def run():
    # Clear old data
    Inventory.objects.all().delete()
    Store.objects.all().delete()
    Book.objects.all().delete()
    Genre.objects.all().delete()
    Author.objects.all().delete()
    Publisher.objects.all().delete()

    # Publishers
    publishers = [
        Publisher.objects.create(name='Alpha Press', country='USA', founded_year=1980),
        Publisher.objects.create(name='Beta Books', country='UK', founded_year=1995),
        Publisher.objects.create(name='Gamma Publishing', country='Kenya', founded_year=2005),
    ]

    # Authors
    authors = [
        Author.objects.create(name='Alice Brown', birth_year=1970, country='USA'),
        Author.objects.create(name='John Doe', birth_year=1985, country='UK'),
        Author.objects.create(name='Mary Njeri', birth_year=1990, country='Kenya'),
        Author.objects.create(name='Carlos Diaz', birth_year=1975, country='Spain'),
    ]

    # Genres
    genres = [
        Genre.objects.create(name='Fiction'),
        Genre.objects.create(name='Technology'),
        Genre.objects.create(name='History'),
    ]

    # Books
    books = []
    for i in range(15):
        book = Book.objects.create(
            title=f'Book {i}',
            pages=random.randint(150, 600),
            price=random.randint(10, 50),
            rating=round(random.uniform(3.0, 5.0), 1),
            publisher=random.choice(publishers),
            publication_year=random.randint(2010, 2024),
        )
        book.authors.set(random.sample(authors, random.randint(1, 2)))
        book.genres.set(random.sample(genres, random.randint(1, 2)))
        books.append(book)

    # Stores
    stores = [
        Store.objects.create(name='Nairobi Books', city='Nairobi'),
        Store.objects.create(name='London Books', city='London'),
    ]

    # Inventory
    for store in stores:
        for book in random.sample(books, 10):
            Inventory.objects.create(
                store=store,
                book=book,
                quantity=random.randint(0, 30)
            )

    print("✅ Database seeded successfully")

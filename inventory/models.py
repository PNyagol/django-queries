from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    founded_year = models.IntegerField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    publisher = models.ForeignKey(
        Publisher,
        related_name='books',
        on_delete=models.CASCADE
    )

    authors = models.ManyToManyField(
        Author,
        related_name='books'
    )

    genres = models.ManyToManyField(
        Genre,
        related_name='books'
    )

    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class Store(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

    books = models.ManyToManyField(
        Book,
        through='Inventory',
        related_name='stores'
    )

    def __str__(self):
        return self.name


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('store', 'book')

import os
import django

# Point to your settings
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'bookstore.settings'
)

# Initialize Django
django.setup()


from inventory.models import Book, Inventory
from django.db.models import Count
from inventory.models import Publisher
from inventory.models import Store
from django.db.models import Sum


print("TOTAL COUNT")
print("Books: ", Book.objects.count())
print("Inventory Rows: ", Inventory.objects.count())


print("\nSAMPLE INVENTORY ROWS")
for row in Inventory.objects.all()[:5]:
    print(f"Store: {row.store.name} | Book: {row.book.title} | Quantity: {row.quantity}")


print("\nSAMPLE INVENTORY ANT")

for inv in Inventory.objects.select_related("store", "book")[:5]:
    print(
        "Store:", inv.store.name,
        "| Book:", inv.book.title,
        "| Qty:", inv.quantity
    )

print("\nBOOKS PER PUBLISHER")

for nyagol in Publisher.objects.annotate(books_count=Count("books")):
    print(nyagol.name, "|", nyagol.books_count)


print("\nSTORES WITH INVENTORY COUNT")

for store in Store.objects.annotate(inventory_count=Count("inventory")):
    print(store.name, "|", store.inventory_count)


print("\nBROKEN QUERY (EXPECTED TO BE WRONG)")

for book in Book.objects.annotate(author_count=Count("authors"), inventory_count=Count("inventory")) [:5]:
    print(book.title, "| Authors:", book.author_count, "| Inventory Rows:", book.inventory_count)


print("\nSEE")

qs = Book.objects.annotate(
    author_count=Count("authors"),
    store_count=Count("inventory"),
)

for b in qs[:5]:
    print(
        b.title,
        "| Authors", b.author_count,
        "| Stores", b.store_count
    )



print("\nFIXED QUERY")

qs = Book.objects.annotate(
    author_count=Count("authors", distinct=True),
    store_count=Count("inventory", distinct=True),
)

for b in qs[:5]:
    print(
        b.title,
        "authors:", b.author_count,
        "stores:", b.store_count
    )


print("\nTOTAL STOCK PER STORE")
for s in Store.objects.annotate(total_stock=Sum("inventory__quantity")):
    print(s.name, "| Total Stock:", s.total_stock)

print("\nWRONG")

qs = Store.objects.annotate(
    total_stock=Sum("inventory__quantity"),
    author_count=Count("inventory__book__authors", distinct=True),
)

for s in qs:
    print(
        s.name,
        "stock:", s.total_stock,
        "authors:", s.author_count
    )

print("\nSEET")
for q in (
    Inventory.objects
    .values("store__name", "book__title")
    .annotate(total_qty=Sum("quantity"))
)[:20]:
    print(q)


print(qs.query)

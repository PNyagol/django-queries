import os
import django

# Point to your settings
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'bookstore.settings'
)

# Initialize Django
django.setup()


from django.db.models import Avg, Count, Sum
from inventory.models import Book, Store


print("\nAGGREGATE EXAMPLE")

stats = Book.objects.aggregate(
    avg_price=Avg('price'),
    total_pages=Sum('pages')
)

print(stats)


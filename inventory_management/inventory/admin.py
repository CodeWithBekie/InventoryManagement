
from django.contrib import admin
from .models import InventoryItem # Import your models

# Register the models to appear in the admin interface
admin.site.register(InventoryItem)


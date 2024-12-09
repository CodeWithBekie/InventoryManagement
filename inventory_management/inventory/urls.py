from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    inventory_list_create,
    inventory_detail,
)


urlpatterns = [
    # Include ViewSet's routes managed by the router
     
    path('inventoryListCreate/', inventory_list_create, name='inventory-list-create'),  # List and Create
    path('inventoryBy/<int:pk>/', inventory_detail, name='inventory-detailed'),   # Retrieve, Update, Delete
]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import InventoryItem
from .serializers import InventoryItemSerializer



# List and Create Inventory Items
@api_view(['GET', 'POST'])
def inventory_list_create(request):
    if request.method == 'GET':
        # Fetch all inventory items
        items = InventoryItem.objects.all()
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new inventory item
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, Update, and Delete a Single Inventory Item
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def inventory_detail(request, pk):
    try:
        # Fetch inventory item by primary key (ID)
        item = InventoryItem.objects.get(pk=pk)
    except InventoryItem.DoesNotExist:
        return Response({'error': 'Inventory item not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Retrieve the item
        serializer = InventoryItemSerializer(item)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        # Update the item
        serializer = InventoryItemSerializer(item, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the item
        item.delete()
        return Response({'message': 'Inventory item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

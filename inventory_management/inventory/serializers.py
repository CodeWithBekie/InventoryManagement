from rest_framework import serializers
from .models import InventoryItem

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'  # Include all fields from the model

    def validate(self, attrs):
        """
        Custom validation logic can be added here.
        For example, check if the quantity is non-negative.
        """
        if attrs.get('quantity', 0) < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return attrs

    def create(self, validated_data):
        """
        Override the create method if you need to customize the creation logic.
        """
        return InventoryItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Override the update method if you need to customize the update logic.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        # Add other fields as necessary
        instance.save()
        return instance
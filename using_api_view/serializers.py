from rest_framework import serializers
from using_api_view.models import CategoryAV, SubCategoryAV, VendorAV, DeliveryAV


class SubCategoryAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryAV
        fields = '__all__'

class VendorAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAV
        fields = '__all__'


class DeliveryAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAV
        fields = '__all__'

class CategoryAVSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryAVSerializer(many=True, read_only=True)
    vendors = VendorAVSerializer(many=True, read_only=True)
    delivery = DeliveryAVSerializer(read_only=True)
    class Meta:
        model = CategoryAV
        fields = ('id', 'category_name', 'sub_categories', 'vendors', 'delivery')

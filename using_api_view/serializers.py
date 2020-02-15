from django.db import transaction
from rest_framework import serializers
from using_api_view.models import CategoryAV, SubCategoryAV, VendorAV, DeliveryAV, Member, Group, \
    Membership


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


"""
Many-to-Many fields using 'through'
"""


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'alias_name', 'groups')
        depth = 1


class GroupMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        depth = 1

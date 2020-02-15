from django.db import models


class CategoryAV(models.Model):
    category_name = models.CharField(max_length=100, blank=False, null=False, unique=True)

    class Meta:
        db_table = 'category_av'

class SubCategoryAV(models.Model):
    sub_category_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    category_av = models.ForeignKey(CategoryAV, on_delete=models.CASCADE, related_name='sub_categories')

    class Meta:
        db_table = 'sub_category_av'

class DeliveryAV(models.Model):
    delivery_address = models.TextField(blank=False, null=False)
    category_av = models.OneToOneField(CategoryAV, on_delete=models.CASCADE, related_name='delivery')

    class Meta:
        db_table = 'delivery_av'

class VendorAV(models.Model):
    vendor_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    category_av = models.ManyToManyField(CategoryAV, related_name='vendors')

    class Meta:
        db_table = 'vendor_av'


"""
Many-to-Many fields using 'through'
"""

class Member(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    alias_name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'member'

class Group(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    members = models.ManyToManyField(Member, related_name='groups', through='Membership')
    # The invisible "through" model that Django uses to make many-to-many relationships work
    # requires the primary keys for the source model and the target model.
    class Meta:
        db_table = 'group'

class Membership(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        db_table = 'membership'
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

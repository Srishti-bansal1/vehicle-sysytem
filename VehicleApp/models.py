from django.db import models
from enum import Enum


# Create your models here.
class UserType(Enum):
    nomal_user= "Normal User"
    quality_check = "Quality Check User"

class QualityCheck(Enum):
    Pass = "PASS"
    Fail = "FAIL"


class User(models.Model):
    name = models.CharField(max_length = 100)
    usertype = models.CharField(max_length = 100 , choices = [(user_type.value, user_type.name) for user_type in UserType ])
    email = models.EmailField()
    password = models.CharField(max_length = 100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

class Vendor (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id'], name='id')
        ]

class Product(models.Model):
    vendor_id = models.ForeignKey(Vendor, default = None,  on_delete = models.CASCADE, related_name='vendor')
    vehicle_photo = models.ImageField(upload_to='Vehicle_Image', null=True, blank=True)
    vehicle_number = models.CharField(max_length = 100)
    vehicle_type = models.CharField(max_length = 100)
    product_quantity = models.CharField(max_length = 100)
    delivery_challan_number = models.CharField(max_length = 100)
    purchase_order_number = models.CharField(max_length = 100)
    purchase_date = models.CharField(max_length = 100)
    quality_check_status = models.CharField(max_length = 100 , choices = [(quality_status.value, quality_status.name) for quality_status in QualityCheck])






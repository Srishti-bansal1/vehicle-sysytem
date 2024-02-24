from .models import User, Vendor, Product
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor_detail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('vendor_detail','vendor_id','vehicle_photo','vehicle_number','vehicle_type','product_quantity','delivery_challan_number','purchase_order_number','purchase_date','quality_check_status')
        
    def get_vendor_detail(self,obj):          #this fun is defind becoz of EDMSmodel don't know about address (but address know about EDMSmodel)
        print(obj)
        vendor_details = Vendor.objects.get(id=obj.vendor_id.id)
        print(vendor_details)
        _serializer = VendorSerializer(vendor_details)
        return _serializer.data
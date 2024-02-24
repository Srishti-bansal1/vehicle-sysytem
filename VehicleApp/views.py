from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.parsers import FormParser
# Create your views here.
from .models import User, Vendor, Product
from .serializers import UserSerializer, VendorSerializer, ProductSerializer, PurchaseOrderSerializer

class UserViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=["GET"],url_path='show_user')
    def getCustom(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True) 
        return Response(serializer.data)
    
    
    @action(detail=False, methods=["POST"],url_path='create_user')
    def created(self, request):
        dataReceived = request.data 
        serializer = UserSerializer(data = request.data)

        if User.objects.filter(**dataReceived).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
    @action(detail=True , methods=['PUT'],url_path='modify_user')
    def modify(self,request,pk=None):
        EDMS = User.objects.get(pk=pk)
        serializer = UserSerializer(instance = EDMS,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=True , methods=['DELETE'],url_path='delete_user')
    def remove(self,request,pk=None):
        EDMS = User.objects.get(pk=pk)  
        EDMS.delete()
        return Response({'message':'data is delete'})
    


class LoginVeiwSet(viewsets.ModelViewSet):
    @action(detail=False, methods=["GET"],url_path='user_access')
    def users_access(self , request):
        _email = request.GET.get('email')
        _password = request.GET.get('password')

        queryset = User.objects.get(email = _email)
        if queryset:
            serializer = UserSerializer(queryset)
        else:
            return Response({'message':'check detail again'}, status= status.HTTP_205_RESET_CONTENT)
        Password = serializer.data.get('password')
        if Password == _password:
            _refresh = RefreshToken()
            token = _refresh.for_user(queryset)
            return Response({"refresh": str(token), "access": str(token.access_token)}) 
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

class VendorViewSet(viewsets.ModelViewSet):        
    @action(detail=False, methods=["GET"],url_path='show_vendor')
    def get_vendor(self , request):
        queryset = Vendor.objects.all()
        if queryset:
            serializer = VendorSerializer(queryset,many = True)
            return Response(serializer.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["POST"],url_path='create_vendor')
    def add_vendor(self, request):
        dataReceived = request.data  

        serializer = VendorSerializer(data = dataReceived )
        
        if Vendor.objects.filter(**dataReceived).exists():
            raise Exception("Duplicate Data")

        if serializer.is_valid():           
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True , methods=['PUT'],url_path='modify_vendor')
    def update_vendor(self,request,pk=None):
        queryset = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(instance = queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    @action(detail=True , methods=['DELETE'],url_path='delete_vendor')
    def remove_vendor(self,request,pk=None):
        queryset = Vendor.objects.get(pk=pk)  
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


class ProductViewSet(viewsets.ModelViewSet):
    #parser_classes = [FormParser]
    @action(detail=False, methods=["GET"],url_path='show_product')
    def get_product(self , request):
        queryset = Product.objects.all()
        if queryset:
            serializer = ProductSerializer(queryset,many = True)
            return Response(serializer.data)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["POST"],url_path='create_product')
    def add_product(self, request):
        dataReceived = request.data  

        __data = {}
        for el in dataReceived:
            __data[el] = dataReceived.get(el)

        serializer = ProductSerializer(data = __data )
        
        if Product.objects.filter(**__data).exists():
            raise Exception("Duplicate Data")

        if serializer.is_valid():           
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=True , methods=['PUT'],url_path='modify_product')
    def update_product(self,request,pk=None):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance = queryset, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    @action(detail=True , methods=['DELETE'],url_path='delete_product')
    def remove_product(self,request,pk=None):
        queryset = Product.objects.get(pk=pk)  
        queryset.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    
    
@api_view(['GET'])   
def SignUp(request):
    return render(request,'signup.html', {'signUp': SignUp})

@api_view(['GET'])   
def Login(request):
    return render(request,'login.html', {'login': Login})


class PurchasrOrderViewSet(viewsets.ReadOnlyModelViewSet):

    @action(detail=False, methods=["GET"],url_path='Purchase-order-no')  
    def detailUser(self, request):
        purchase_order_number = int(request.GET['purchase_order_number'])
        print(purchase_order_number)
        queryset = Product.objects.filter(purchase_order_number=purchase_order_number)
        print(queryset)
        serializer = PurchaseOrderSerializer(queryset, many=True) 
        print(serializer.data)
        return Response(serializer.data)
    
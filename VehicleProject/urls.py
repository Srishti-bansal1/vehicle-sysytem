"""
URL configuration for VehicleProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from VehicleApp import views
from VehicleApp.views import PurchasrOrderViewSet, UserViewSet, LoginVeiwSet, VendorViewSet, ProductViewSet, VehicleViewSet, CheckoutViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API docs ",
      default_version='v1',
      description="Vehicle managemant sysytem",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter(trailing_slash=False)
router.register(r'user_signUp',UserViewSet, basename='user_signUp')
router.register(r'user_logIn', LoginVeiwSet, basename='user_logIn')
router.register(r'vendor', VendorViewSet, basename='vendor')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'vehicle', VehicleViewSet, basename='vehicle')
router.register(r'status', CheckoutViewSet, basename='status')
router.register(r'purchase-no', PurchasrOrderViewSet, basename='purchase-no')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('USER/', include(router.urls)),
    path('sigup', views.SignUp , name='signup'),
    path('login', views.Login , name='login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

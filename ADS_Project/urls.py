"""
URL configuration for ADS_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
#from . import views
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.login_page, name='login'),  # Root URL for loginpg.html
    path('ecommerce_website/', views.ecommerce_website_page, name='ecommerce_website'),  # URL for ecommerce_website.html
    path('signup/', views.signup_page, name='signup'),  # URL for signup.html
    path('gaming-laptops/', views.gaming_laptops, name='gaming_laptops'),
    path('gaming-laptops/search/', views.search_laptops, name='filter_search'),
    path('study-laptops/search/', views.search_laptops, name='filter_search'),
    path('office-laptops/search/', views.search_laptops, name='filter_search'),
    path('study-laptops/', views.study_laptops, name='study_laptops'),
    path('office-laptops/', views.office_laptops, name='office_laptops'),
    path('search/', views.search_laptops_by_model, name='search_laptops_by_model'),
    path('laptop/<int:laptop_id>/', views.laptop_details, name='laptop_details'),
    path('address/',views.address,name='address'),
    path('payment/',views.payment,name='payment')





]
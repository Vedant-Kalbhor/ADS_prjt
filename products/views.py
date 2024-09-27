from django.shortcuts import render

def login_page(request):
    return render(request, 'products/loginpg.html')  # Rendering loginpg.html

def ecommerce_website_page(request):
    return render(request, 'products/ecommerce_website.html')  # Rendering ecommerce_website.html

def signup_page(request):
    return render(request, 'products/signup.html')  # Rendering signup.html

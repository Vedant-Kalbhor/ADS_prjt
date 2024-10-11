from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from .models import Laptop
# from .avl_graph import LaptopAVL, LaptopGraph  # Assuming you placed the classes in avl_graph.py
from django.core.cache import cache
from .models import Product
from .avl_graph import AVLTree, search_products_by_price

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User  # Assuming you placed the classes in avl_graph.py


#fyddydyduyd
def login_page(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Correct credentials, log the user in
            login(request, user)

            # Optionally handle the 'Remember me' functionality
            if 'remember_me' in request.POST:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Session expires when the browser is closed

            # Redirect to the homepage or user dashboard
            return redirect('ecommerce_website')
        else:
            # Invalid credentials, return an error message
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

     return render(request, 'products/loginpg.html' ,)  # Rendering loginpg.html

def ecommerce_website_page(request):
    return render(request, 'products/ecommerce_website.html')  # Rendering ecommerce_website.html

def signup_page(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        
        if password != repeat_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'products/signup.html')

        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=firstname)
            user.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page after successful signup
        except Exception as e:
            messages.error(request, "User creation failed: " + str(e))
            return render(request, 'products/signup.html')
    return render(request, 'products/signup.html')  # Rendering signup.html


def ecommerce_website_page(request):
    return render(request, 'products/ecommerce_website.html')  # Rendering ecommerce_website.html


def gaming_laptops(request):
    return render(request, 'products/gaming_laptops.html')

def study_laptops(request):
    return render(request, 'products/study_laptops.html')

def office_laptops(request):
    return render(request, 'products/office_laptops.html')
def  address(request):
    return render(request, 'products/address.html')
def  payment(request):
    return render(request, 'products/payment.html')



# from django.shortcuts import render, get_object_or_404
# from .models import Laptop

# def search_laptops(request):
#     query = request.GET.get('query', '')  # Get the search query
#     laptops = Laptop.objects.filter(model_name__icontains=query) if query else Laptop.objects.all()
#     return render(request, 'products/search_results.html', {'laptops': laptops})
def build_avl_tree():
    avl_tree = AVLTree()
    root = None
    for laptop in Laptop.objects.all():
        root = avl_tree.insert(root, laptop)
    return root

def update_tree_cache():
    # Rebuild and cache the AVL tree when products change
    root = build_avl_tree()
    cache.set('avl_tree', root, timeout=None)  # Cache indefinitely

def laptop_search(request):
    filters = {
        'price_min': float(request.GET.get('price_min', 0)),
        'price_max': float(request.GET.get('price_max', float('inf'))),
        'processors': request.GET.getlist('processor'),
        'graphics_cards': request.GET.getlist('graphics_card'),
        'companies': request.GET.getlist('company'),
        'display_size': request.GET.getlist('display_size'),
    }

    # Retrieve the AVL tree from cache
    root = cache.get('avl_tree')

    if not root:
        # If tree not found in cache, build and cache it
        root = build_avl_tree()
        cache.set('avl_tree', root, timeout=None)

    # Step 1: Search by price range using the AVL tree
    min_price = filters['price_min']
    max_price = filters['price_max']
    products_in_price_range = search_products_by_price(root, min_price, max_price)

    # Step 2: Filter based on checkbox options
    filtered_products = []
    for product in products_in_price_range:
        if filters['processors'] and product.processor not in filters['processors']:
            continue
        if filters['graphics_cards'] and product.graphics_card not in filters['graphics_cards']:
            continue
        if filters['companies'] and product.company not in filters['companies']:
            continue
        if filters['display_size'] and product.display_size not in filters['display_size']:
            continue
        filtered_products.append(product)

    # Render the results
    return render(request, 'search_results.html', {'products': filtered_products})

def laptop_details(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    return render(request, 'products/details.html', {'laptop': laptop})


# from django.shortcuts import render
# from .models import Laptop
# from .avl_graph import LaptopAVL, LaptopGraph  # Assuming you placed the classes in avl_graph.py

def search_by_price(request):
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 10000)

    # Initialize and build the BST with all laptops
    laptop_avl = LaptopAVL()
    laptops = Laptop.objects.all()
    for laptop in laptops:
        laptop_avl.insert(laptop)

    # Search for laptops within the price range
    laptops_in_range = laptop_avl.search_by_price_range(float(min_price), float(max_price))

    return render(request, 'products/search_results.html', {'laptops': laptops_in_range})


def related_laptops(request, laptop_id):
    laptop = Laptop.objects.get(id=laptop_id)

    # Initialize and build the Graph with all laptops
    laptop_graph = LaptopGraph()
    all_laptops = Laptop.objects.all()
    for lap in all_laptops:
        laptop_graph.add_laptop(lap)

    # Get related laptops by brand and type
    related_laptops = laptop_graph.get_related_laptops(laptop)

    return render(request, 'products/related_laptops.html', {'laptops': related_laptops, 'laptop': laptop})

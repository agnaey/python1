from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Product, Cart, Order
# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("/")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already taken"})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("home")
    return render(request, "register.html")



def home(request):
    return render(request, "home.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, "cart.html", {"cart_items": cart_items})

def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('cart_view')

def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == "POST":
        phone = request.POST["phone"]
        address = request.POST["address"]

        order = Order.objects.create(user=request.user, phone=phone, address=address, total_amount=total)
        cart_items.delete()
        return redirect("home")

    return render(request, "checkout.html", {"cart_items": cart_items, "total": total})

def ordered_products(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "ordered_products.html", {"orders": orders})




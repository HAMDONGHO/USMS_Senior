from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Order
from bboard.models import Post

# Create your views here.
def home(request):
    orders = Order.objects
    posts = Post.objects
    return render(request, 'home.html', {'orders' : orders, 'posts':posts})
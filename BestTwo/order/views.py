from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Order
from bboard.models import Post
from __future__ import print_function
import grpc
import gigagenieRPC_pb2
import gigagenieRPC_pb2_grpc
import MicrophoneStream as MS
import user_auth as UA
import audioop
import os
import time
import case1 as kws
import CCTV as cctv
from ctypes import *

# Create your views here.
def home(request):
    orders = Order.objects
    posts = Post.objects
    return render(request, 'home.html', {'orders' : orders, 'posts':posts})
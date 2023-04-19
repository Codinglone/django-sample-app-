from django.shortcuts import render, HttpResponse
from .models import Sneakers
# Create your views here.
def index(response):
    shoes = Sneakers.objects.all()

    return render(response, "main/index.html", {"shoes": shoes})
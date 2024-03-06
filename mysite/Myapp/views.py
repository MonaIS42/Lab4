from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):

    return  HttpResponse("This is a site to calculate tax.")


tax_rate = 0.15


def newprice(request, num):

    price = num + (num*tax_rate)
    return  HttpResponse(f"The price with 15% tax is: {price}")


def taxrate(request):

    return  HttpResponse(f"The tax rate is: {tax_rate}")




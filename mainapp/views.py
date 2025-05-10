from django.shortcuts import render
import requests

def index(request):
    return render (request, 'stockpicker/index.html')

# def stockpicker(request):
#     return render(request, 'mainapp/stockpicker.html')

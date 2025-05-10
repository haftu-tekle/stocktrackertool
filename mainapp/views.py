from django.shortcuts import render
import requests

def stockpicker(request):
    return render(request, 'mainapp/stockpicker.html')
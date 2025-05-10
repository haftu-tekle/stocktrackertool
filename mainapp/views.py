from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import django_bootstrap5

def index(request):
    return render(request, 'stockpicker/index.html',{})
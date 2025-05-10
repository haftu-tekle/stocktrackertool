
from django.urls import path,include
from . import views
# import templates
from mainapp import b

urlpatterns = [
    
   path('mainapp/templates/mainapp/stockpicker', views.stockpicker, name='stockpicker')
]

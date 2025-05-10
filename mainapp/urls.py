
from django.urls import path
from . import views
# import templates


urlpatterns = [
    
   path('', views.index, name='index')
]

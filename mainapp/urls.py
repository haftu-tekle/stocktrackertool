from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('table.html', views.stockTracker,name='stockTracker')
    
]

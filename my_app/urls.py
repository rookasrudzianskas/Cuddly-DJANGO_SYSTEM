from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search/', views.new_searches, name='new_search'),
]

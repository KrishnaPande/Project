from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    # Passing a Dynamic Value 59:07
    path('room/<str:pk>/', views.room, name="room"),
]
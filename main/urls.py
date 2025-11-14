from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('notes/', views.ListNotesView.as_view(), name='notes'),
    path('calculate/', views.calculate, name='calculate'),
]
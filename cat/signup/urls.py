# signup/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add root path here
    path('submit/', views.submit_person, name='submit_person'),
    path('success/', views.success_view, name='success'),
]

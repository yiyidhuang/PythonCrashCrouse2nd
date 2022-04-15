from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Contains the default authentication URL
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]

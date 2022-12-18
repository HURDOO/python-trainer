from django.urls import path, include
from . import views

app_name = 'manito'
urlpatterns = [
    path('', views.main),
    path('about/', views.about)
]
from django.urls import path
from . import views

app_name = 'submit'
urlpatterns = [
    path('new', views.new),
    path('', views.submit),
    path('<int:submit_id>', views.detail),
    path('result_info', views.result_info)
]

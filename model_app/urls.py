from django.urls import  path
from .views import  data_detail


urlpatterns = [
    path('users/', data_detail),
]

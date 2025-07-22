

from django.contrib import admin
from django.urls import path , include
# from django.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('model_app/', include('model_app.urls')),
]

from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', views.hello_user),
    path('api/get-products/', views.fetch_products),
]

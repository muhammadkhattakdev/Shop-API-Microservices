from django.contrib import admin
from django.urls import path
from emails.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/test-email/', test_mail)
]

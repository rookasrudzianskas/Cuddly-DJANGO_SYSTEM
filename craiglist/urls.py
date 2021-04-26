from django.contrib import admin
from django.urls import path, include

import my_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(my_app.urls)),
]

from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

import EmployeeApp

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(EmployeeApp.urls)),
]

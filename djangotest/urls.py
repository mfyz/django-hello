from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include

urlpatterns = [
	path('books/', include('books.urls')),
    path('admin/', admin.site.urls),
]

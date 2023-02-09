from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'))#O include ele pede como parâmetro um array, que seria o no caso o url.
]

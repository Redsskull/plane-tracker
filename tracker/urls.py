from django.contrib import admin
from django.urls import path,include
from planes import views as planes

urlpatterns = [
    path('', planes.index, name = 'planes'),
    path('admin/', admin.site.urls),
]

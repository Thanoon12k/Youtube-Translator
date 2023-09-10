
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('video2textapp.urls')),  # Including urls of `myapp`

]

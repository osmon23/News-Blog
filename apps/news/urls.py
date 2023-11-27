from django.urls import path

from .views import get, detail

urlpatterns = [
    path('', get, name='index'),
    path('detail/<int:pk>', detail, name='detail')
]

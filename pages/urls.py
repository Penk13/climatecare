from django.urls import path

from .views import homepage

app_name = 'page'
urlpatterns = [
    path('', homepage, name='homepage'),
]

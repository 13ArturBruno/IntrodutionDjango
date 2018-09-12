from django.urls import path, include
from .views import home, produto

urlpatterns = [
    path('', home),
    path('produto/<int:codigo>/', produto)
]
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path("", views.products, name='products'),
    path("<int:product_id>/", views.detail, name='detail'),
]
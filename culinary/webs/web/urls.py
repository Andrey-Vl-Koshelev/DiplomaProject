from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogweb, name='blogweb'),
    path('blog/<str:pk>/', views.blog, name='blog'),

    path('current/', views.currentweb, name='currentweb'),
]

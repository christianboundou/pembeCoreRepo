from django.urls import path

from blog import views

urlpatterns = [
    path('', views.list, name='list'),
    path('post/<int:pk>/', views.show, name='show'),
]

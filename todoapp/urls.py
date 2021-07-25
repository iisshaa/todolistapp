from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='todo-home'),
    path('update/<int:pk>/', views.update, name='todo-update'),
    path('delete/<int:pk>/', views.delete, name='todo-delete'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),

]

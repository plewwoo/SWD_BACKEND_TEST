from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('todo-list', TodoListAPIView.as_view(), name='todo-list.apiview'),
    path('todo-update/<int:pk>', TodoListUpdateAPIView.as_view(), name='todo-update.apiview'),
]

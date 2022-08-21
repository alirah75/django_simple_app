from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.sey_hello, name='sey_hello'),
    path('details/<int:todo_id>', views.details, name='details'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('create', views.create, name='create'),
    path('update/<int:todo_id>', views.update, name='update'),
]

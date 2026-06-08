from django.urls import path
from . import views

app_name = 'sosmed'

urlpatterns = [
    path('', views.home, name='home'),

    path('<str:platform>/', views.list_sosmed, name='list'),
    path('<str:platform>/create/', views.create, name='create'),
    path('<str:platform>/update/<int:update_id>/', views.update, name='update'),
    path('<str:platform>/delete/<int:delete_id>/', views.delete, name='delete'),
]

from django.urls import path
from . import views

app_name = 'sosmed'

urlpatterns = [
    path('', views.home, name='home'),

    path('instagram/', views.list_instagram, name='list'),
    path('create/', views.create, name='create'),
    path('update/<int:update_id>/', views.update, name='update'),
    path('delete/<int:delete_id>/', views.delete, name='delete'),

    path('tiktok/', views.tiktok, name='tiktok'),
    path('facebook/', views.facebook, name='facebook'),
    path('twitter/', views.twitter, name='twitter'),
]

from django.contrib import admin
from django.urls import path
from index import views


urlpatterns = [
   
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('selling/', views.selling, name='selling'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
    # path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('about/', views.about, name='about'),

 ]

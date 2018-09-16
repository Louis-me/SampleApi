from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),
    path('save_shop', views.save_shop, name='save_shop'),
    path('get_shop_list', views.get_shop_list, name='get_shop_list'),


]
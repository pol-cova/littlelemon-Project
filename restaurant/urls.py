from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/menu/', views.MenuItemsViews.as_view(), name='menu'),
    path('restaurant/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
]
from django.urls import path, include
from . import views

# Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingView, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurant/menu/', views.MenuItemsViews.as_view(), name='menu'),
    path('restaurant/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('restaurant/bookings/', include(router.urls)),
]
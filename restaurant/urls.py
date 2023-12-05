from django.urls import path, include
from . import views

# Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingView, basename='booking')

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items/', views.MenuItemsViews.as_view(), name='menu'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('bookings/', include(router.urls)),
]
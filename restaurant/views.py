from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
# Models and serializers
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Custom class permission
# Manager or read only permission class
class ManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Allow read only permissions for safe methods
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Check if user is a manager or staff
        if request.user.is_authenticated and request.user.groups.filter(name='Manager').exists() or request.user.is_staff:
            return True

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
    

# Menu API
class MenuItemsViews(ListCreateAPIView):
    permission_classes = [ManagerOrReadOnly]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Single Menu Item API
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Booking API
class BookingView(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
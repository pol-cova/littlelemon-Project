from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Models and serializers
from .models import Menu, Booking
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
    

# Menu API
class MenuItemsViews(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Single Menu Item API
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
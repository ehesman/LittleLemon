from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menu, Booking
from .serializers import BookingSerializer, MenuSerializer,UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.decorators import api_view
#from .models import MenuItem
#from .serializers import MenuItemSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class bookingview(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer= BookingSerializer(items, many=True)
        return Response(serializer.data) # Return JSON
    
class menuview(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer= MenuSerializer(items, many=True)
        return Response(serializer.data) # Return JSON  

    def post(self, request):
        serializer= MenuSerializer(data=request, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
"""
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 
"""
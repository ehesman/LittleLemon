#define URL route for index() view
from django.urls import path,include
from . import views
from .views import menuview, bookingview

urlpatterns = [
    #path('', views.index, name='index'),
    #path('menu/', menuview.as_view()),
    #path('booking/', bookingview.as_view()),
    path('items/', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('', include('router.urls')),
    #('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

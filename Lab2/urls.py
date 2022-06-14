"""Lab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Lab2_1.views.client_view import ClientListCreateAPIView, ClientRetrieveUpdateAPIView
from Lab2_1.views.csv_view import UploadDataCSVFile
from Lab2_1.views.hotel_chain_view import HotelChainListCreateAPIView, HotelChainRetrieveUpdateAPIView
from Lab2_1.views.hotel_view import HotelListCreateAPIView, HotelRetrieveUpdateAPIView
from Lab2_1.views.message_view import MessageListCreateAPIView, MessageRetrieveUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('clients/', ClientListCreateAPIView.as_view()),
    path('clients/<int:pk>/', ClientRetrieveUpdateAPIView.as_view()),

    path('hotel_chains/', HotelChainListCreateAPIView.as_view()),
    path('hotel_chains/<int:pk>/', HotelChainRetrieveUpdateAPIView.as_view()),

    path('hotels/', HotelListCreateAPIView.as_view()),
    path('hotels/<int:pk>/', HotelRetrieveUpdateAPIView.as_view()),

    path('messages/', MessageListCreateAPIView.as_view()),
    path('messages/<int:pk>/', MessageRetrieveUpdateAPIView.as_view()),

    path('test_csv/', UploadDataCSVFile.as_view()),
]

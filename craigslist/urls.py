from django.urls import path

from .views import *

urlpatterns = [
    path('', allListings, name='listings'),
    path('listing/<int:pk>/', listingDetail, name='listing'),
    path('listing-create/', listingCreate, name='listing-create'),

]

from django.urls import path
from .views import ( buy_car,show_details,update_car,delete_car )

urlpatterns = [
    path('buy_car/',buy_car,name='buy_car'),
    path('show_cars/',show_details,name='show_details'),
    path('update_car/<int:pk>/',update_car,name='update_car'),
    path('delete_car/<int:pk>/',delete_car,name='delete_car')
]
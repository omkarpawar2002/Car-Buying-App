from django.urls import path
from .views import ( login_view,register,logout_view )

urlpatterns = [
    path('login/',login_view,name='login_url'),
    path('signup/',register,name='signup_url'),
    path('logout/',logout_view,name='logout_url')
]
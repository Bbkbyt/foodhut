from django.urls import path
from .views import user_register

app_name='accounts'
urlpatterns = [
    path('signup/',user_register,name='signup'),
]
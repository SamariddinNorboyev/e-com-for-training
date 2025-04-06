from django.urls import path

from order.urls import app_name
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'profile_info'
urlpatterns = [
    path('', views.ProfileUpdateView.as_view(), name='profile')
]
from django.urls import path
from . import views
from .api import views as api_views
urlpatterns = [
    path('',api_views.api_home,name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/<slug:slug>/',views.details, name='details'),
    path('booking/',views.booking, name='booking')

]
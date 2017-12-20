from django.urls import path
from . import views

urlpatterns = [
    path('dummy/', views.index, name='index'),
    path('signout/', views.signout, name='signout'),
]

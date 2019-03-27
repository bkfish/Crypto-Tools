from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index1, name='index1'),

]
from django.urls import path

from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('hexAscii/', views.hexAscii, name='hexAscii'),
    path('urlCode/', views.urlCode, name='urlCode'),
    path('morse/', views.morse, name='morse'),
    path('morseTable/', views.morseTable, name='morseTable'),
    path('converter/', views.converter, name='converter'),
    path('caesar/', views.caesar, name='caesar'),
    path('fence/', views.fence, name='fence'),
    path('bacon/', views.bacon, name='bacon'),
    path('jsfuck/', views.jsfuck, name='jsfuck'),
    path('rsa/', views.rsa, name='rsa'),
    path('fac/', views.fac, name='fac'),
    path('moder/', views.moder, name='moder'),
    path('commode/', views.commode, name='commode'),
    path('rsascript/', views.rsascript, name='rsascript'),
    

]
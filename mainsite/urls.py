from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_login , name = 'show_login' ) ,
    path('logup/', views.show_logup , name = 'show_logup' ) ,
    path('log_up/', views.sign_up , name = 'sign_up' ) ,
    path('log_in/', views.sign_in , name = 'sign_in' ) ,
]

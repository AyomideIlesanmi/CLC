from django.urls import path
from . import views
 
urlpatterns = [
    path('number_pyramid/<int:number>/', views.number_pyramid, name='number_pyramid'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('user_data/', views.user_data, name='user_data'),
    path('ajax_search/', views.ajax_search, name='ajax_search'),
]
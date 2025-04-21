
from django.urls import path
from . import views

urlpatterns = [

   
    path('', views.home, name="home"),
    
    path('create-account', views.create_account, name="create-account"),

    path('my-login', views.my_login, name="my-login"),
    path('dashboard', views.dashboard, name ="dashboard"),
    path ('logout-user', views.logout_user, name="logout-user"),
    path('create-contact', views.create_contact, name="create-contact"),
    path('update-contact/<int:pk>/', views.update_contact, name="update-contact"),

   
     path('delete-contact/<int:pk>/', views.delete_contact, name='delete-contact'),


   
    path('record/<int:pk>/', views.singular_contact, name='record'),
   



    
    
]
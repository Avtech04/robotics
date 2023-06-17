from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' ,  home  , name="home"),
    path('register' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    # path('contacts' , contacts , name='contacts'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('downloadUser' , user_list , name="downloadUser"),
    # path('accounts/contacts' , contacts , name="contacts"),
    path('accounts/logout/' , logout_attempt , name="logout_attempt"),
    path('accounts/usersDetail' , usersDetail , name="usersDetail"),
    path('accounts/delete/<str:username>/' , delete_user , name="delete_user"),
    path('accounts/modify/<str:username>/' , modify_user , name="modify_user"), 


    path('contact/', contact, name='contact'),


]

from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='articles'

urlpatterns = [ 
     path('', views.article_list, name='list'),
     path('create/', views.article_create, name='create'),
     path('<slug:slug>/', views.article_details, name='detail'),
]


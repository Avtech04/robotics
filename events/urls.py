from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path('',views.event,name='events'),
    path('event/<str:id>',views.eventpost,name='eventpost'),
    path('create_event/', views.create_event, name='create_event'),
    path('add', views.ADD_event, name='add'),
    path('edit', views.Edit_event, name='edit'),
    path('update/<str:id>', views.Update_event, name='update'),
    path('delete/<str:id>', views.Delete_event, name='delete'),
    path('search', views.search_event, name='search'),
    path('register_participant/', views.register_participant, name='register_participant'),
    path('registered_events/', views.participant_registered_events, name='participant_registered_events')
]   
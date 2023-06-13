from django.contrib import admin
from django.urls import path
from noticeBoard import views

urlpatterns = [
    path("", views.adminNotice, name='noticeBoard'),
    path("adminNotice", views.adminNotice, name='adminNotice'),
    path("addNotice", views.addNotice, name='addNotice'),
    path("delete/<int:id>/", views.delete_data, name='deletedata'),
    path("<int:id>/", views.update_data, name='updatedata'),
    path("broadcast/<int:id>/", views.broadcast, name='broadcastdata'),
   
   
]
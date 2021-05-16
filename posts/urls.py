from django.contrib import admin
from django.urls import path
from .views import (home_view, post_detail_view, post_list_view, 
post_create_view, post_delete_view,post_actions_view, )

urlpatterns = [
    path('', post_list_view),
    path('create/', post_create_view),
    path('action/', post_actions_view),
    path('<int:post_id>/', post_detail_view),
    path('<int:post_id>/delete/' , post_delete_view)
]

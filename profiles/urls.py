from django.urls import path
from .views import profile_detail_views


urlpatterns=[
    path('<str:username>', profile_detail_views)


]
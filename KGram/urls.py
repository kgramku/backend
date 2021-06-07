"""KGram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path , include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from posts.views import (home_view, post_detail_view, post_list_view, 
post_create_view, post_delete_view,post_actions_view, )

from accounts.views import( login_view, registration_view, logout_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('posts/', post_list_view),
    path('posts/<int:post_id>', post_detail_view),
    path('create-post', post_create_view),
    path('api/posts/',include('posts.urls')),
    re_path(r'profiles?/',include('profiles.urls')),
    # path('', include("django.contrib.auth.urls")),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', registration_view),

    #api documentationurl
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='docs.html'),
    path('openapi/', get_schema_view(
            title="Your Project",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
]






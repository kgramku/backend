from django.shortcuts import render

# Create your views here.

def profile_detail_views(request, username, *args, **kwargs):
    return render(request,"profiles/detail.html",{'username': username})


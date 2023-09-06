
from django.contrib import admin
from django.urls import path,include
from .views import register,log_in,download,home,api_viewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r"api",api_viewset)
urlpatterns = [
    path('admin/', admin.site.urls), #for admin panel
    path("",home,name='name'), #for home
    path("signup/",register.as_view(),name='signup'), #for signup the user
    path("login/",log_in.as_view(),name='logup'),#for login the user
    path("download/<int:id>",download.as_view(),name='gettdata'),#for download the file the user
    path("getdata",include(router.urls)),#for retrive data the user
    path("auth/",include('rest_framework.urls')),
]

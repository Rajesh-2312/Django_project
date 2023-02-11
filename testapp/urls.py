from urllib.parse import urlparse
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('video',views.video,name='video'),
    path('about',views.about,name='about'),
    path('contents',views.contents,name='contents'),
    path('home',views.home,name='home'),
]

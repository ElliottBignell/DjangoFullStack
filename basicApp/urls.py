from django.conf.urls import url
from django.urls import path, re_path
from basicApp import views

# TEMPLATE URLS
app_name = 'basicApp'

urlpatterns = [
    re_path( r'register/$', views.register, name='register' ),
    re_path( '^user_login/$', views.user_login, name='user_login' )
]

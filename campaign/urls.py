from campaign import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
         path('register', views.registerPage, name="register"),
	     path('login', views.loginPage, name="login"),  
	     path('logout', views.logoutUser, name="logout"),
    path('', views.home.as_view(), name='home'),
    path('file', views.fiels,name='files'),
    path('form', views.form,name='form'),
    path('list', views.list.as_view(),name='list'),
   
]
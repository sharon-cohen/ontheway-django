from campaign import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import form
from django.conf.urls import include, url
urlpatterns = [
         path('register', views.registerPage, name="register"),
	     path('login', views.loginPage, name="login"),  
	     path('logout', views.logoutUser, name="logout"),
    path('', views.home, name='home'),
    path('form', views.form.as_view(),name='form'),
    path('list', views.list,name='list'),
    path('profile', views.profile ,name='profile'),
    path('item/<int:item_pk>', views.item, name='item'),
    path('updateFile/<int:item_pk>', views.updateFiles, name='updateFile'),
    path('update/<int:item_pk>', views.update, name='update'),
    path('item/<int:item_pk>/delete', views.delete, name='delete'),
    path('item/<int:item_pk>/deletefile', views.deletefile, name='deletefile'),
    path('messages', views.messagesPage, name='messages'),
]
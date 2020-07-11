from campaign import views
from django.urls import path


urlpatterns = [
    path('', views.home.as_view(),),
    path('file', views.fiels,name='files'),
    path('form', views.form,name='form'),
]
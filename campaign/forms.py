from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import File, Campaign

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['user','name','duration','category','location','around','picture','num_file']
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['num_file','name','RoadType','percent', 'dayTime','picture']
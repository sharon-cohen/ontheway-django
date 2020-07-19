from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import File, Campaign,Profile

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['user','name','duration','category','location','around','picture','num_file']
        widgets = {'user': forms.HiddenInput()}
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['num_file','name','RoadType','percent', 'dayTime','picture']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    email=forms.EmailField(required=False)
    company=forms.CharField(required=False)
    role= forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = ['picture','company','email','role' ]
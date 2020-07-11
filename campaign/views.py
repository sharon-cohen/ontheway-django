

# from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import File, Campaign
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm
from django.utils.decorators import method_decorator
# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
			

        context = {'form':form}
        return render(request, 'campaign/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'campaign/login.html', context)

@method_decorator(login_required, name='dispatch')
class home(generic.ListView):
    queryset = Campaign.objects.all()
    template_name = 'campaign/index.html'


def logoutUser(request):
	logout(request)
	return redirect('login')
@login_required(login_url='login')

def form(request):
    CampaignFormSet=modelformset_factory(Campaign, fields=('user','name','duration','category','location','around','picture'),extra=1)
    if request.method =='POST':
        form=CampaignFormSet(request.POST,request.FILES)
        if form.is_valid():
          
            instances = form.save(commit=False)		
            instances=request.user
            instances=form.save()
    form=CampaignFormSet(queryset=Campaign.objects.none())
    return render(request,'campaign/form.html',{'form' : form})

@login_required(login_url='login')



def fiels(request):
    name = request.GET.get('numFile', '')
    if name=="3":
        FileFormSet=modelformset_factory(File, fields=('name','RoadType','percent', 'dayTime','picture'),extra=3)
    if name=="2":
       FileFormSet=modelformset_factory(File, fields=('name','RoadType','percent', 'dayTime','picture'),extra=2)
    if name=="1":
       FileFormSet=modelformset_factory(File, fields=('name','RoadType','percent', 'dayTime','picture'),extra=1)
    if request.method =='POST':
        forms=FileFormSet(request.POST)
        if forms.is_valid():
            instances= forms.save()
    forms=FileFormSet(queryset=File.objects.none())
    return render(request,'campaign/file.html', {'forms' : forms})
  
class list(generic.ListView):
    queryset = Campaign.objects.all()
    template_name = 'campaign/list.html'


	
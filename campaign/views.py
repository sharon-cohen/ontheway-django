

# from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import File, Campaign, Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm, CampaignForm, FileForm , UserUpdateForm, ProfileUpdateForm
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.contrib.auth.models import Group
from .filters import CampFilter
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def registerPage(request):
    context = Campaign.objects.all()
    camp_filter = CampFilter(request.GET, queryset=context)
    if request.user.is_authenticated:
        return render(request, 'campaign/index.html',{'campaign_list':context,'filter': camp_filter})
    else:
        form = CreateUserForm(request.POST)
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                print(username)
			#Added username after video because of error returning customer name if not added
                Profile.objects.create(
                user=user,
                name=user.username,
				)
                new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
                login(request, new_user)
                messages.success(request, 'Account was created for ' + username)
                
                
                return render(request, 'campaign/index.html',{'campaign_list':context,'filter': camp_filter})
			

        context = {'form':form}
        return render(request, 'campaign/register.html', context)

def loginPage(request):
    context = Campaign.objects.all()
    camp_filter = CampFilter(request.GET, queryset=context)
    if request.user.is_authenticated:
        return render(request, 'campaign/index.html',{'campaign_list':context,'filter': camp_filter})
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'campaign/index.html',{'campaign_list':context,'filter': camp_filter})
            else:
                messages.info(request, 'Username OR password is incorrect')
      
        context = Campaign.objects.all()
        return render(request, 'campaign/login.html')


def home(request):
    camps_list = Campaign.objects.all()
    camp_filter = CampFilter(request.GET, queryset=camps_list)
    return render(request, 'campaign/index.html',{'campaign_list':camps_list,'filter': camp_filter})

@method_decorator(login_required, name='dispatch')
class form(generic.ListView):
    template_name = 'campaign/form.html'
  
    def get(self, request):
        username=request.user
        print(username)
        form = CampaignForm()
        form.initial['user'] = username 
       
        return render(request, self.template_name,{'form':form})
    def post(self, request):
        
        form1=CampaignForm(request.POST,request.FILES)
        if request.method =='POST':
           
            if form1.is_valid():
               
                instances = form1.save()		
                instances=request.user
                instances=form1.save() 
                text = form1.cleaned_data['num_file']
                num=int(text)
                cmpname=form1.cleaned_data['name']
                FileFormSet=modelformset_factory(File, fields=('campName','name','RoadType','percent', 'dayTime','picture','num_file'),extra=num,)
                form2=FileFormSet(queryset=Campaign.objects.none())
                for form in form2:
                    form.initial['campName'] = cmpname
                return render(request, 'campaign/form.html',{'forms':form2})
            else:
                if request.method =='POST':
                    FileFormSet=modelformset_factory(File, fields=('campName','name','RoadType','percent', 'dayTime','picture','num_file'),)
                    form2=FileFormSet(request.POST,request.FILES)
                    if form2.is_valid():
                        instances= form2.save()
                    
                        return render(request, 'campaign/form.html',{'forms':form2})


def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')

def list(request):
    camps = Campaign.objects.all()
    return render(request, 'campaign/list.html', {'camps': camps})

def item(request,item_pk):
    current_user = request.user
    print(current_user)
    
    print(item_pk)
    item = get_object_or_404(Campaign, pk=item_pk)
    fiels=File.objects.all()

    if request.method == 'GET':
        return render(request, 'campaign/item.html', {'object': item,'user':current_user,'files':fiels})
   
       
        
def update(request,item_pk):
    camp = get_object_or_404(Campaign, pk=item_pk)
    current_user = request.user
    
    if request.method == 'GET':
        form = CampaignForm(instance=camp)
        return render(request, 'campaign/update.html', {'camp': camp, 'form': form})
    else:
        try:
            form = CampaignForm(request.POST, instance=camp)
            form.save()
            return redirect('list')
        except ValueError:
            return render(request, 'campaign/update.html', {'form': CampaignForm(), 'errMsg': 'Data mismatch'})
def updateFiles(request,item_pk):
    camp = get_object_or_404(File, pk=item_pk)
    if request.method == 'GET':
        form = FileForm(instance=camp)
        return render(request, 'campaign/update.html', {'camp': camp, 'form': form})
    else:
        try:
            form = FileForm(request.POST, instance=camp)
            form.save()
            return redirect('list')
        except ValueError:
            return render(request, 'campaign/update.html', {'form': FileForm(), 'errMsg': 'Data mismatch'})
def updateprofil(request,item_pk):
    camp = get_object_or_404(User, pk=item_pk)
    if request.method == 'GET':
        form = FileForm(instance=camp)
        return render(request, 'campaign/update.html', {'camp': camp, 'form': form})
    else:
        try:
            form = FileForm(request.POST, instance=camp)
            form.save()
            return redirect('list')
        except ValueError:
            return render(request, 'campaign/update.html', {'form': FileForm(), 'errMsg': 'Data mismatch'})

def delete(request, item_pk):
    camp = get_object_or_404(Campaign, pk=item_pk)
    if request.method == 'POST':
        camp.delete()
        return redirect('list')

def profile(request):
   
    objects = Profile.objects.all()
    for object in objects:
       
        if(object.user.username == request.user.username):
            myobject=object
           
        
    print(myobject.user)
    if request.method == 'GET':
        p_form = ProfileUpdateForm(instance=myobject)
        return render(request, 'campaign/profile.html', {'p_form':p_form})
    else:
        try:
            p_form = ProfileUpdateForm(request.POST,request.FILES,instance=myobject)
            p_form.save()
            return redirect('profile')
        except ValueError:
            return render(request, 'campaign/profile.html',{'p_form':p_form})
    
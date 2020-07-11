

# from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import File, Campaign
from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
# Create your views here.

def form(request):
    CampaignFormSet=modelformset_factory(Campaign, fields=('name','duration'),extra=1)
    if request.method =='POST':
        form=CampaignFormSet(request.POST)
        instances = form.save()		
    form=CampaignFormSet(queryset=Campaign.objects.none())
    return render(request,'campaign/form.html',{'form' : form})

class home(generic.ListView):
    queryset = Campaign.objects.all()
    template_name = 'campaign/index.html'
 
def fiels(request):
    name = request.GET.get('numFile', '')
    if name=="3":
        FileFormSet=modelformset_factory(File, fields=('name','display'),extra=3)
    if name=="2":
        FileFormSet=modelformset_factory(File, fields=('name','display'),extra=2)
    if name=="1":
        FileFormSet=modelformset_factory(File, fields=('name','display'),extra=1)

    if request.method =='POST':
        forms=FileFormSet(request.POST)
        if forms.is_valid():
            instances= forms.save()
    forms=FileFormSet(queryset=File.objects.none())
    return render(request,'campaign/file.html', {'forms' : forms})
	

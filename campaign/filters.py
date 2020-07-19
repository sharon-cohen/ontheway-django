import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

from django.contrib.auth.models import User
import django_filters

class CampFilter(django_filters.FilterSet):
    class Meta:
        model = Campaign
        fields = [ 'name', 'status']
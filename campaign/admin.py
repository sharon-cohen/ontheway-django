from django.contrib import admin

# Register your models here.

from .models import Campaign
from .models import File,Profile
admin.site.register(Campaign)
admin.site.register(File)
admin.site.register(Profile)
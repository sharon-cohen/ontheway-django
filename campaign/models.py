
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
# Create your models here.

DURATION = (
    ('One week', 'One week'),
    ('Two weeks', 'Two weeks'),
    ('one month', 'One month')
)

  
CATEGORY = (
    ('Food', 'Food'),
    ('Beauty, Care and Health', 'Beauty, Care and Health'),
    ('Fation', 'Fation'),
    ('Home Products', 'Home Products'),
)
 
LOCATION = (
     ('Tel Aviv Metropolitan Area', 'Tel Aviv Metropolitan Area'),
     ('Jerusalem', 'Jerusalem'),
     ('North', 'North'),
     ('South','South')
)
 
ROADTYPE = (
    ('High-Way', 'High-Way'),
    ('Urban', 'Urban'),
    ('Inter-Urban-Roads', 'Inter-Urban-Roads'),
)
AROUND = (
    ('schools', 'schools'),
    ('Offices', 'Offices'),
    ('shopping centers', 'shopping centers'),
)
PERCENTׂ = (
   ('10%','10%'),
   ('20%','20%'),
   ('30%','30%'),
   ('40%','40%'),
   ('50%','50%'),
   ('60%','60%'),
   ('70%','70%'),
   ('80%','80%'),
   ('90%','90%'),
   ('100%','100%'),
)

DAYTIME = (
  ('Morning','Morning'),
  ('Noon','Noon'),
  ('Evening','Evening'),
)

STATUSE = (
    ('process', 'process'),
    ('done', 'done'),
    ('wait', 'wait'),
    ('running', 'running')
)


class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1, related_name='blog_posts')
    name = models.CharField(max_length=200, null=True)
    status =models.CharField(max_length=30,choices=STATUSE, default='wait')
    duration =models.CharField(max_length=30,choices=DURATION , default='One week')
    category =models.CharField(max_length=30,choices=CATEGORY, default='Food')
    location =models.CharField(max_length=50,choices=LOCATION, default='Tel Aviv Metropolitan Area')
    around =models.CharField(max_length=50,choices=AROUND, default='shools')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    url=models.URLField(blank=True)
    picture = models.ImageField(upload_to='campaign/images', default='')
    def __str__(self):
        return self.name
        
class Meta:
    ordering = ['-created_on']


class File(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    RoadType = models.CharField(max_length=20,choices=ROADTYPE, default='High-Way')
    percent =models.CharField(max_length=20,choices=PERCENTׂ, default='10%')
    dayTime = models.CharField(max_length=20,choices=DAYTIME, default='Morning')
    picture = models.ImageField(upload_to='campaign/images', default='')
    
    def __str__(self):
        return self.name    







from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DURATION = (
    ('One manth', 'One manth'),
    ('Two manths', 'Two manths'),
    ('Tree manths', 'Tree manths')
)

  
CATEGORY = (
    ('Food', 'Food'),
    ('Beauty, Care and Health', 'Beauty, Care and Health'),
    ('Fation', 'Fation'),
    ('Home Products', 'Home Products'),
)
 
AREAS = (
     ('Tel-Aviv', 'Tel-Aviv'),
     ('Jerusalem', 'Jerusalem'),
     ('North', 'North'),
)
 
DISPLAY = (
    ('High-Way', 'High-Way'),
    ('Urban', 'Urban'),
    ('Inter-Urban-Roads', 'Inter-Urban-Roads'),
)
STATUSE = (
    ('process', 'process'),
    ('done', 'done'),
    ('wait', 'wait'),
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

DAY = (
  ('Morning','Morning'),
  ('Noon','Noon'),
  ('Evening','Evening'),
)

class Campaign(models.Model):
    name = models.CharField(max_length=200, null=True)
    duration =models.CharField(max_length=30,choices=DURATION , default='One manth')
    category =models.CharField(max_length=30,choices=CATEGORY, default='Food')
    areas =models.CharField(max_length=10,choices=AREAS , default='Tel-Aviv')
    status =models.CharField(max_length=20,choices=STATUSE , default='wait')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    url=models.URLField(blank=True)
    picture = models.ImageField(upload_to='campaign/images', default='')
    def __str__(self):
        return self.name
        
class Meta:
    ordering = ['-created_on']


class File(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    display = models.CharField(max_length=20,choices=DISPLAY, default='High-Way')
    percent =models.CharField(max_length=20,choices=PERCENTׂ, default='10%')
    day = models.CharField(max_length=20,choices=DISPLAY, default='Morning')
    url=models.URLField(blank=True)
    
    def __str__(self):
        return self.name    



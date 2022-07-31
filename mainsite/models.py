from asyncio.windows_events import NULL
from django.db import models

class users(models.Model):
    full_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50 , blank = True)
    last_name = models.CharField(max_length=50 , blank = True)
    password_user = models.CharField(max_length=100)
    dateTimeFild = models.DateTimeField(auto_now = True)
    email_user = models.CharField(max_length=100 , blank = True)
    number_of_user = models.IntegerField(blank = True , default=0 )
    info = models.CharField(max_length=1000 , blank = True)
    

class posts(models.Model):
    user = models.ForeignKey( users , on_delete=models.CASCADE , default= -1)
    contint = models.CharField(max_length=50 , blank = True )
    number_liks = models.IntegerField()
    number_comment = models.IntegerField()
    info = models.CharField(max_length=50 , blank = True)
    dateTimeFild = models.DateTimeField(auto_now = True)


from django.db import models
from utilityapp.models import Address
from django.contrib.auth.models import AbstractUser



# Create your models here.
class ProfileUser(AbstractUser):
    phone_num = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    bio = models.TextField()
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_profile')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.username
    
    class Meta:
        
        db_table = 'usertable'  
    
    
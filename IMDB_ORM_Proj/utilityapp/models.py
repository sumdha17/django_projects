from django.db import models
from .choices import CATEGORY_CHOICES, STATE_CHOICES, LANGUAGE_CHOICES, AWARD_NAME_CHOICES

# Create your models here.
class Common(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        abstract = True  # Ensures Common is treated as an abstract model

class Address(Common):
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank= True, null=True)
    area = models.CharField(max_length=200)
    pincode = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, choices=STATE_CHOICES)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city
    class Meta:
        db_table = 'address'  
        unique_together = ('line1', 'pincode')             # in line 1 we write buliding or house num then it have unique pincode
    
class Category(Common):
    category_name = models.CharField(max_length=200)
    category_type = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    
    
    def __str__(self): 
        return self.category_name
    
    class Meta:
        db_table = 'category'  
        unique_together = ('category_name', 'category_type')
        
        
class Language(Common):
    language_name = models.CharField(max_length=100, choices=LANGUAGE_CHOICES)
    
    def __str__(self):
        return self.language_name
    
    class Meta:
        db_table = 'language'  
    


class Awards(Common):
    award_name = models.CharField(max_length=100, choices=AWARD_NAME_CHOICES)
    description = models.TextField()
    establisment_year = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='awards')       # category have multiple awards
    
    def __str__(self):
        return self.award_name
    
    class Meta:
        db_table = 'awards'   
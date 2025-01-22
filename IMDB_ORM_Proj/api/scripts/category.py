from utilityapp.models import Category
from django.db.models import Count
from utilityapp.choices import CATEGORY_CHOICES
# 
    
    
    
def delete_duplicate():
    categories = Category.objects.values('category_name', 'category_type').annotate(count_num=Count('category_name')).filter(count_num__gt=1)
    for category in categories:
        duplicates_category = Category.objects.filter(category_name=category['category_name'], category_type=category['category_type'])
        # write the nested loop delete the all duplicates
        for category in duplicates_category[1:]:
            category.delete()


def create_bulk_catagory():
    l = []
    category_name_list = ["Actor", "Comedy", "Horror", "Drama"]
    for category_name in category_name_list:
        for category_type in CATEGORY_CHOICES:
            l.append(Category(category_name=category_name, category_type=category_type[0]))
    Category.objects.bulk_create(l)
    
            
    
            

            
        
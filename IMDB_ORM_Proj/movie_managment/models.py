from django.db import models
from utilityapp.models import Address, Category, Awards
from utilityapp.choices import GENDER_CHOICES
from userapp.models import ProfileUser
# Create your models here.

class ProductionHouse(models.Model):
    production_name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    founded_year = models.PositiveIntegerField()
    website_url = models.URLField(max_length=500, blank=True, null=True)
    facebook_url = models.URLField(max_length=500, blank=True, null=True)
    twitter_url = models.URLField(max_length=500, blank=True, null=True)
    youtube_url = models.URLField(max_length=500, blank=True, null=True)
    instagram_url = models.URLField(max_length=500, blank=True, null=True)
    domains = models.TextField()  # Stores a list of domains as a comma-separated string
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    logo = models.ImageField(upload_to='media/logos/', blank=True, null=True)
    address =  models.OneToOneField(Address, on_delete=models.CASCADE, related_name='production_house')       # one production house have one address

    def __str__(self):
        return self.production_name
    class Meta:
        db_table = 'productionhouse'  
        
        
        
class Crew(models.Model): 
    crew_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    net_worth = models.DecimalField(max_digits=15, decimal_places=2)
    date_of_birth = models.DateField()
    about = models.TextField()
    occupations = models.TextField()  # Stores a list of occupations as a comma-separated string
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='crew')     #One address can be associated with multiple crew members

    def __str__(self):
        return self.crew_name
    class Meta:
        db_table = 'crew'  
        
class Language(models.Model):
    lan_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.lan_name
    
    class Meta:
        db_table = 'mm_language'  
        

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=255)
    duration = models.DurationField()
    song_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, related_name='song')
    released_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.song_name
    class Meta:
        db_table = 'song'  
        
        
class Collection(models.Model):
    box_office_collections = models.DecimalField(max_digits=15, decimal_places=2)
    advertisement = models.DecimalField(max_digits=15, decimal_places=2)
    domestic_collection = models.DecimalField(max_digits=15, decimal_places=2)
    gross = models.DecimalField(max_digits=15, decimal_places=2)
    first_date = models.DecimalField(max_digits=15, decimal_places=2)
    first_week = models.DecimalField(max_digits=15, decimal_places=2)
    first_month = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Collection ID: {self.id}"
    class Meta:
        db_table = 'collections'  
        
class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, limit_choices_to={'category_type':'movie'}, related_name='movie_category')        # one category with many movies
    duration = models.DurationField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='movie_language')                # one language with many movies

    def __str__(self):
        return self.movie_name
    
    class Meta:
        db_table = 'movie'  
        
        
class MovieReview(models.Model):
    movie_rating = models.DecimalField(max_digits=3, decimal_places=1)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moviereview')            
    movie_user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, related_name='moviereview_user')             # delete user rating also delete
    comment = models.TextField()

    def __str__(self):
        return self.movie.movie_name
    
    class Meta:
        db_table = 'movie_review'  

class MusicReview(models.Model):
    music_rating = models.DecimalField(max_digits=3, decimal_places=1)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='musicreview')
    music_user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE, related_name='user_musicreview') 
    comment = models.TextField()

    def __str__(self):
        return self.song.song_name

    class Meta:
        db_table = 'music_review'  
        
class DistributionHouse(models.Model):
    d_house_name = models.CharField(max_length=200)  # The name of the distribution house
    contacts = models.TextField()  # A field for contact details (could be a list or detailed description)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='distribution_house')  # ForeignKey to Address
    phone = models.CharField(max_length=15)  # Phone number
    email = models.EmailField()  # Email address
    description = models.TextField()  # Description of the distribution house

    def __str__(self):
        return self.d_house_name
    class Meta:
        db_table = 'distribution_house'  
        

class MovieCrew(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_crew')
    crew_id = models.ForeignKey(Crew, on_delete=models.SET_NULL, null=True, blank=True, related_name='crew_movie')
    crew_category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='crewcategory')
    
    def __str__(self):
        return self.movie_id.movie_name
    class Meta:
        db_table = 'moviecrew'  

    
    
class MovieMusic(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_music')
    song_id = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True, blank=True, related_name='music_movie')
    music_category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='musiccategory')
    
    def __str__(self):
        return self.movie_id.movie_name
    class Meta:
        db_table = 'moviemusic' 
        
class MovieCollection(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_collection')
    collection_id = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True, related_name='collection_movie')
    collection_cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='collectioncategory')
    
    def __str__(self):
        return self.movie_id.movie_name
    
    class Meta:
        db_table = 'moviecollection' 
        
        
class AwardCrew(models.Model):
    award_id = models.ForeignKey(Awards, on_delete=models.SET_NULL, null=True, blank=True, default=1, related_name='awardcrew')
    crew_id = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name='crewaward')
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.crew_id.crew_name
    class Meta:
        db_table = 'awardcrew' 
        
class AwardSong(models.Model):
    award_id = models.ForeignKey(Awards, on_delete=models.SET_NULL, null=True, blank=True, related_name='award_song')
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_award')
    year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.song_id.song_name
    class Meta:
        db_table = 'awardsong' 
        
class MovieAward(models.Model):
    award_id = models.ForeignKey(Awards, on_delete=models.SET_NULL, null=True, blank=True, related_name='award_movie')
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_award')
    year = models.PositiveIntegerField()
    
    def __str__(self):
        return self.movie_id.movie_name
    class Meta:
        db_table = 'movieaward' 
    
    
    
        

    
    

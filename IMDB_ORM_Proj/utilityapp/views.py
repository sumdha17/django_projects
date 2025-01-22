from django.shortcuts import render

# Create your views here.
'''
from userapp.models import *
from movie_managment.models import *
from utilityapp.models import *

add1 = Address.object.create(line1 = 'Dehu Phata', area='Aalandi', pincode=412105, city='Pune',
state='Maharashtra', country='India')          

aw =Awards.objects.create(award_name= "Oskar", description= "Awarded for the best overall film of the year.",establisment_year= 1929, category= c[0])

Address.objects.all()                #fetch all adresses in database
<QuerySet [<Address: Pune>]>

Address.objects.all().values()
<QuerySet [{'id': 1, 'created_at': datetime.date(2025, 1, 3), 'updated_at': datetime.date(2025, 1, 3), 'line1': 'Dehu Phata', 'line2': None,
'area': 'Aalandi', 'pincode': 412105, 'city': 'Pune', 'state': 'Maharashtra', 'country': 'India'}]>

list(Address.objects.all().values())
[{'id': 1, 'created_at': datetime.date(2025, 1, 3), 'updated_at': datetime.date(2025, 1, 3), 
'line1': 'Dehu Phata', 'line2': None, 'area': 'Aalandi', 'pincode': 412105, 'city': 'Pune',
'state': 'Maharashtra', 'country': 'India'}]


a1 = Address.objects.bulk_create([Address(line1='Dehu Phata', line2='Moshi', area='Aalandi', pincode=412105, city='Pune', state='Maharashtra', country='India'),Address(line1='Sector 4', line2='Nigdi', area='Pradhikaran', pincode=411044, city='Pune', state='Maharashtra', country='India')
,Address(line1='Katraj Chowk', line2='Bharti Vidyapeeth', area='Katraj', pincode=411046, city='Pune', state='Maharashtra', country='India'),Address(line1='MG Road', line2='Camp', area='Pune Camp', pincode=411001, city='Pune', state='Maharashtra', country='India'),
Address(line1='Shivaji Nagar', line2='Jungli Maharaj Road', area='Shivaji Nagar', pincode=411005, city='Pune', state='Maharashtra', country='India'),Address(line1='Baner Road', line2='Balewadi', area='Baner', pincode=411045, city='Pune', state='Maharashtra', country='India'),
Address(line1='Hinjewadi Phase 1', line2='Rajiv Gandhi Infotech Park', area='Hinjewadi', pincode=411057, city='Pune', state='Maharashtra', country='India'),])

a1 = Address.objects.get(id=1)    
user = ProfileUser.objects.create_user(username='user5', phone_num='7876564520', image=None, bio='Bio for user5', address=a1) 

c = Category.objects.bulk_create([Category(category_name='Actor', category_type='crew'),
Category(category_name='Director', category_type='crew'),Category(category_name='Actress', category_type='crew'), 
Category(category_name='Best Actor', category_type='Award'),Category(category_name='Best Picture', category_type='Award'),
Category(category_name='Comedy', category_type='movie'),Category(category_name='Horror', category_type='movie'),
Category(category_name='Drama', category_type='movie'),Category(category_name='Comedy', category_type='movie'),
Category(category_name='Best Song', category_type='Award')])


c = Category.objects.all()
aw =Awards.objects.create(award_name= "Oskar", description= "Awarded for the best overall film of the year.",establisment_year= 1929, category= c[0])
aw =Awards.objects.create(award_name= "Oskar", description= "Awarded for the best overall film of the year.",establisment_year= 1929, category= c[5]) 
aw =Awards.objects.create(award_name= "Oskar", description= "Awarded for the best Actor of the year.",establisment_year= 1929, category= c[4])    

c = Category.objects.all()
aw =Awards.objects.bulk_create([Awards(award_name= "National Award", description= "Awarded for the best song of the year.",establisment_year= 1969, category= c[9]),Awards(award_name= "Filmfare", description= "Awarded for the best Actor of the year.",establisment_year= 1955, category= c[3]),Awards(award_name= "IIFA", description= "Awarded for the best picture of the year.",establisment_year= 1971, category= c[4]),Awards(award_name= "IIFA Award", description= "Awarded for the best Actor of the year.",establisment_year= 1971, category= c[3]),Awards(award_name= "IIFA Award", description= "Awarded for the best song of the year.",establisment_year= 1969, category= c[9]),Awards(award_name= "FilmFare", description= "Awarded for the best song of the year.",establisment_year= 1969, category= c[9])])


p = ProductionHouse.objects.create(production_name="Reliance Entertainment",owner="Anil Ambani",founded_year=2005,website_url="https://www.relianceentertainment.com/",facebook_url= "https://www.facebook.com/RelianceEnt/",twitter_url="https://x.com/RelianceEnt",youtube_url="https://www.youtube.com/@RelianceEnt",instagram_url= "https://www.instagram.com/reliance.entertainment/",domains="Movies",phone_number="+9134567890",email="re.info@restudios.co.in",logo= None, address=ad[2])  

p = ProductionHouse.objects.create(production_name="Dharma Productions ",owner="Karan Johar",founded_year=1979,website_url="https://www.dharma-production.com/",facebook_url= "https://www.facebook.com/DharmaMovies/",twitter_url="https://x.com/DharmaMovies",youtube_url="https://www.youtube.com/channel/UCKQKIY2YlI4L5QVg7hhfjrQ",instagram_url= "https://www.instagram.com/dharmamovies/",domains="Movies",phone_number="+9134561234",email="re.info@restudios.co.in",logo= None, address=ad[4]) 


cr = Crew.objects.bulk_create([(crew_name="A. R. Rahman", gender="Male", net_worth=80000000.00, date_of_birth="1967-01-06", about="Indian music composer, singer, and music producer, known as 'The Mozart of Madras'.", occupations="Singer", 
    address=ad[0]),Crew(crew_name="Rajkumar Hirani", gender="Male", net_worth=10000000.00,date_of_birth="1962-11-20", about="Indian filmmaker known for his films '3 Idiots' and 'PK'.", occupations="Director", 
    address=ad[1]),Crew(crew_name="Priyanka Chopra", gender="Female", net_worth=70000000.00, date_of_birth="1982-07-18", about="Indian actress, producer, and global icon known for her work in Bollywood and Hollywood.", occupations="Actor", address=ad[2]),Crew(crew_name="Sanjay Leela Bhansali",gender="Male", net_worth=30000000.00, date_of_birth="1963-02-24", about="Indian director and producer known for visually stunning films like 'Padmaavat' and 'Devdas'.", occupations="Director", 
    address=ad[3]),Crew(crew_name="Vidya Balan", gender="Female", net_worth=25000000.00, date_of_birth="1979-01-01", about="Indian actress known for her roles in films like 'Kahaani' and 'The Dirty Picture'.", occupations="Actor", 
    address=ad[5]),Crew(crew_name="Deepika Padukone", gender="Female", net_worth=40000000.00, date_of_birth="1986-01-05", about="Indian actress and producer known for her roles in 'Padmaavat' and 'Chennai Express'.", occupations="Actor, Producer", 
    address=ad[7]),Crew(crew_name="Amitabh Bachchan", gender="Male", net_worth=500000000.00, date_of_birth="1942-10-11", about="Legendary Indian actor known as the 'Shahenshah' of Bollywood.", occupations="Actor", 
    address=ad[8])])
    
    
Language.objects.bulk_create([Language(lan_name="Hindi"),    Language(lan_name="English"),    Language(lan_name="Marathi"),    Language(lan_name="Tamil"),    
Language(lan_name="Telugu"),    Language(lan_name="Bengali"),    Language(lan_name="Punjabi")])

l = Language.objects.all()    
s = Song.objects.bulk_create([Song(song_name="Tum Hi Ho", duration=timedelta(minutes=4, seconds=30), song_language=l[0], released_date="2013-04-15", description="A romantic Bollywood song from Aashiqui 2."),
    Song(song_name="Vennilave", duration=timedelta(minutes=5, seconds=0), song_language=l[3], released_date="1999-01-01", description="A soulful love song from the movie Minsara Kanavu."),
    Song(song_name="Butta Bomma", duration=timedelta(minutes=3, seconds=45), song_language=l[4], released_date="2020-01-01", description="A hit song from the movie Ala Vaikunthapurramuloo."),
    Song(song_name="Laung Laachi", duration=timedelta(minutes=3, seconds=50), song_language=l[6], released_date="2018-02-14", description="A superhit Punjabi song from the movie Laung Laachi."),
    Song(song_name="Tumi Jaake Bhalobasho", duration=timedelta(minutes=4, seconds=15), song_language=l[5], released_date="2016-12-30", description="A romantic Bengali song from the movie Baishe Srabon."),
    Song(song_name="Chaiyya Chaiyya", duration=timedelta(minutes=5, seconds=30), song_language=l[0], released_date="1998-09-12", description="A popular Bollywood song from the movie Dil Se."),
    Song(song_name="Rowdy Baby", duration=timedelta(minutes=4, seconds=10), song_language=l[3], released_date="2018-12-28", description="A peppy Tamil song from the movie Maari 2."),
    Song(song_name="Pakka Local", duration=timedelta(minutes=3, seconds=20), song_language=l[4], released_date="2017-10-14", description="A popular mass number from the movie Janatha Garage."),
    Song(song_name="Mundian To Bach Ke", duration=timedelta(minutes=3, seconds=40), song_language=l[6], released_date="1998-09-22", description="A globally recognized Punjabi song by Panjabi MC."),
    Song(song_name="Amar Sonar Bangla", duration=timedelta(minutes=3, seconds=0), song_language=l[5], released_date="1905-01-01", description="A patriotic Bengali song written by Rabindranath Tagore.")]) 
    
col = Collection.objects.bulk_create([Collection(
        box_office_collections=Decimal('100000000.00'),
        advertisement=Decimal('5000000.00'),
        domestic_collection=Decimal('50000000.00'),
        gross=Decimal('150000000.00'),
        first_date=Decimal('3000000.00'),
        first_week=Decimal('15000000.00'),
        first_month=Decimal('30000000.00')
    ),
    Collection(
        box_office_collections=Decimal('120000000.00'),
        advertisement=Decimal('6000000.00'),
        domestic_collection=Decimal('60000000.00'),
        gross=Decimal('170000000.00'),
        first_date=Decimal('3500000.00'),
        first_week=Decimal('17000000.00'),
        first_month=Decimal('35000000.00')
    ),
    Collection(
        box_office_collections=Decimal('90000000.00'),
        advertisement=Decimal('4000000.00'),
        domestic_collection=Decimal('45000000.00'),
        gross=Decimal('130000000.00'),
        first_date=Decimal('2500000.00'),
        first_week=Decimal('12000000.00'),
        first_month=Decimal('25000000.00')
    ),
    Collection(
        box_office_collections=Decimal('80000000.00'),
        advertisement=Decimal('3500000.00'),
        domestic_collection=Decimal('40000000.00'),
        gross=Decimal('110000000.00'),
        first_date=Decimal('2000000.00'),
        first_week=Decimal('10000000.00'),
        first_month=Decimal('22000000.00')
    ),
    Collection(
        box_office_collections=Decimal('150000000.00'),
        advertisement=Decimal('7000000.00'),
        domestic_collection=Decimal('70000000.00'),
        gross=Decimal('180000000.00'),
        first_date=Decimal('4000000.00'),
        first_week=Decimal('20000000.00'),
        first_month=Decimal('42000000.00')
    ),
    Collection(
        box_office_collections=Decimal('95000000.00'),
        advertisement=Decimal('4500000.00'),
        domestic_collection=Decimal('47000000.00'),
        gross=Decimal('140000000.00'),
        first_date=Decimal('2700000.00'),
        first_week=Decimal('13000000.00'),
        first_month=Decimal('28000000.00')
    ),
    Collection(
        box_office_collections=Decimal('130000000.00'),
        advertisement=Decimal('6500000.00'),
        domestic_collection=Decimal('65000000.00'),
        gross=Decimal('160000000.00'),
        first_date=Decimal('3200000.00'),
        first_week=Decimal('16000000.00'),
        first_month=Decimal('33000000.00')
    ),
    Collection(
        box_office_collections=Decimal('110000000.00'),
        advertisement=Decimal('5500000.00'),
        domestic_collection=Decimal('55000000.00'),
        gross=Decimal('150000000.00'),
        first_date=Decimal('3000000.00'),
        first_week=Decimal('15000000.00'),
        first_month=Decimal('31000000.00')
    ),
    Collection(
        box_office_collections=Decimal('105000000.00'),
        advertisement=Decimal('5300000.00'),
        domestic_collection=Decimal('52000000.00'),
        gross=Decimal('145000000.00'),
        first_date=Decimal('2900000.00'),
        first_week=Decimal('14000000.00'),
        first_month=Decimal('30000000.00')
    ),
    Collection(
        box_office_collections=Decimal('140000000.00'),
        advertisement=Decimal('6800000.00'),
        domestic_collection=Decimal('68000000.00'),
        gross=Decimal('175000000.00'),
        first_date=Decimal('3600000.00'),
        first_week=Decimal('18000000.00'),
        first_month=Decimal('37000000.00')
    )])
    


m = Movie.objects.bulk_create([
    Movie(
        movie_name="Dilwale Dulhania Le Jayenge",
        release_date="1995-10-20",
        description="A classic Bollywood romance starring Shah Rukh Khan and Kajol.",
        category=c[7],  
        duration=timedelta(minutes=180),
        language=l[0]  
    ),
    Movie(
        movie_name="3 Idiots",
        release_date="2009-12-25",
        description="A comedy-drama about the lives of three engineering students.",
        category=c[5],  
        duration=timedelta(minutes=170),
        language=l[0]  
    ),
    Movie(
        movie_name="Bahubali: The Beginning",
        release_date="2015-07-10",
        description="A historical epic set in the kingdom of Mahishmati.",
        category=c[7],  
        duration=timedelta(minutes=159),
        language=l[4]
    ),
    Movie(
        movie_name="Kabhi Khushi Kabhie Gham",
        release_date="2001-12-14",
        description="A family drama that spans generations of a rich family.",
        category=c[7], 
        duration=timedelta(minutes=210),
        language=l[0] 
    ),
    Movie(
        movie_name="Dangal",
        release_date="2016-12-23",
        description="A biographical sports drama based on wrestler Mahavir Singh Phogat.",
        category=c[7],  
        duration=timedelta(minutes=161),
        language=l[0]  
    ),
    Movie(
        movie_name="Lagaan",
        release_date="2001-06-15",
        description="A historical sports drama where villagers fight against the British.",
        category=c[7],
        duration=timedelta(minutes=224),
        language=l[0]  
    ),
    Movie(
        movie_name="Kahaani",
        release_date="2012-03-09",
        description="A thriller about a pregnant woman searching for her missing husband.",
        category=c[6],
        duration=timedelta(minutes=122),
        language=l[0]  
    ),
    Movie(
        movie_name="Makkhi",
        release_date="2012-10-12",
        description="A fantasy action film about reincarnation and revenge.",
        category=c[5], 
        duration=timedelta(minutes=129),
        language=l[4]  
    ),
    Movie(
        movie_name="Queen",
        release_date="2013-03-07",
        description="A comedy-drama about a woman who embarks on a solo honeymoon trip.",
        category=c[6],  
        duration=timedelta(minutes=146),
        language=l[0]  
    ),
    Movie(
        movie_name="Zindagi Na Milegi Dobara",
        release_date="2011-07-15",
        description="A road trip film about three friends who re-discover themselves.",
        category=c[7],  
        duration=timedelta(minutes=155),
        language=l[0]  
    )
])
    
'''

'''
from myapp.models import MyModel

# Create objects
obj = MyModel.objects.create(field_name='value', another_field=42)

# Retrieve all objects
all_objects = MyModel.objects.all()

# Retrieve a single object
single_object = MyModel.objects.get(pk=1)

# Filter objects
filtered_objects = MyModel.objects.filter(field_name='value')

# Chaining filters
chained_filters = MyModel.objects.filter(field_name='value', another_field=42)

# Exclude objects
excluded_objects = MyModel.objects.exclude(field_name='value')

# Ordering
ordered_objects = MyModel.objects.order_by('field_name')

# Count objects
count_objects = MyModel.objects.count()

# Check if an object exists
exists = MyModel.objects.filter(field_name='value').exists()

# Delete objects
MyModel.objects.filter(field_name='value').delete()


m_c = MovieCrew.objects.bulk_create([MovieCrew(movie_id=movie[1], crew_id=crew[2], crew_category_id=category[5]),    
MovieCrew(movie_id=movie[8], crew_id=crew[4], crew_category_id=category[6]),
MovieCrew(movie_id=movie[4], crew_id=crew[5], crew_category_id=category[7]),    
MovieCrew(movie_id=movie[5], crew_id=crew[6], crew_category_id=category[8]),    
MovieCrew(movie_id=movie[6], crew_id=crew[2], crew_category_id=category[5]),    
MovieCrew(movie_id=movie[7], crew_id=crew[4], crew_category_id=category[6])'''

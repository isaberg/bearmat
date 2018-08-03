from django.db import models
from viewflow.models import Process
from localflavor.us.models import USZipCodeField, USStateField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


# validating here in models rather than mess with CreateView in my View-Form process...

class User(AbstractUser):
    is_veteran = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location_zip = USZipCodeField()
    location_state = USStateField()
    profile_url = models.TextField('profile picture URL', null=True, blank=True)
    org_name = models.CharField('organization name', max_length=100)
    org_url = models.TextField('organization website', null=True, blank=True)
    education = models.CharField('summary of education', max_length=280)
    bio = models.CharField('short biography', max_length=280)
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

class Search(models.Model):
    STATE_CHOICES = (
    ('AL', 'Alabama'),('AK', 'Alaska'),('AZ', 'Arizona'),('AR', 'Arkansas'),
    ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'),
    ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'),
    ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'),
    ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
    ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
    ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
    ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
    ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
    ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'), ('WY', 'Wyoming')
    )
    ADMINISTRATION = 1
    AGRICULTURE = 2
    AUTOMOTIVE = 3
    CONSULTING = 4
    DEFENSE = 5
    DESIGN = 6
    EDUCATION = 7
    ENERGY = 8
    EVENTS = 9
    FINANCE = 10
    FOOD = 11
    HEALTH = 12
    HOSPITALITY = 13
    INSURANCE = 14
    LEGAL = 15
    MANUFACTURING = 16
    RE = 17
    RETAIL = 18
    SERVICES = 19
    SOFTWARE = 20
    STORAGE = 21
    TECHNOLOGY = 22
    TRADES = 23
    TRANSPORTATION = 24
    WASTEMGMT = 25
    INDUSTRY_CHOICES = (
    ('ADMINISTRATION', 'Administration'),('AGRICULTURE', 'Agriculture'),
    ('AUTOMOTIVE', 'Automotive'),('CONSULTING', 'Consulting'),
    ('DEFENSE', 'Defense'), ('DESIGN', 'Design'), ('EDUCATION', 'Education'),
    ('ENERGY', 'Energy'), ('EVENTS', 'Events'), ('FINANCE', 'Financial Services'),
    ('FOOD', 'Food'), ('HEALTH', 'Health Care'), ('HOSPITALITY', 'Tourism & Hospitality'),
    ('INSURANCE', 'Insurance'), ('LEGAL', 'Legal Services'), ('MANUFACTURING', 'Manufacturing'),
    ('RE', 'Real Estate'), ('RETAIL', 'Retail'), ('SERVICES', 'Professional & Consumer Services'),
    ('SOFTWARE', 'Software'), ('STORAGE', 'Storage'), ('TECHNOLOGY', 'Technology'), ('TRADES', 'Trades'),
    ('TRANSPORTATION', 'Transportation'), ('WASTEMGMT', 'Waste Management')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='searches')
    name = models.CharField('search title', max_length=75)
    early = models.DateField('earliest full time start date')
    late = models.DateField('latest full time start date')
    state = models.CharField(
        'states of interest',
        choices=STATE_CHOICES,
        default='MT',
        max_length=100
    )
    industry = models.CharField(
        'industries of interest',
        max_length=100,
        choices=INDUSTRY_CHOICES,
        default='TRADES'
    )
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Business(models.Model):
    STATE_CHOICES = (
    ('AL', 'Alabama'),('AK', 'Alaska'),('AZ', 'Arizona'),('AR', 'Arkansas'),
    ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'),
    ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'),
    ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'),
    ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
    ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'),
    ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
    ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),
    ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
    ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'), ('WY', 'Wyoming')
    )
    ADMINISTRATION = 1
    AGRICULTURE = 2
    AUTOMOTIVE = 3
    CONSULTING = 4
    DEFENSE = 5
    DESIGN = 6
    EDUCATION = 7
    ENERGY = 8
    EVENTS = 9
    FINANCE = 10
    FOOD = 11
    HEALTH = 12
    HOSPITALITY = 13
    INSURANCE = 14
    LEGAL = 15
    MANUFACTURING = 16
    RE = 17
    RETAIL = 18
    SERVICES = 19
    SOFTWARE = 20
    STORAGE = 21
    TECHNOLOGY = 22
    TRADES = 23
    TRANSPORTATION = 24
    WASTEMGMT = 25
    INDUSTRY_CHOICES = (
    ('ADMINISTRATION', 'Administration'),('AGRICULTURE', 'Agriculture'),
    ('AUTOMOTIVE', 'Automotive'),('CONSULTING', 'Consulting'),
    ('DEFENSE', 'Defense'), ('DESIGN', 'Design'), ('EDUCATION', 'Education'),
    ('ENERGY', 'Energy'), ('EVENTS', 'Events'), ('FINANCE', 'Financial Services'),
    ('FOOD', 'Food'), ('HEALTH', 'Health Care'), ('HOSPITALITY', 'Tourism & Hospitality'),
    ('INSURANCE', 'Insurance'), ('LEGAL', 'Legal Services'), ('MANUFACTURING', 'Manufacturing'),
    ('RE', 'Real Estate'), ('RETAIL', 'Retail'), ('SERVICES', 'Professional & Consumer Services'),
    ('SOFTWARE', 'Software'), ('STORAGE', 'Storage'), ('TECHNOLOGY', 'Technology'), ('TRADES', 'Trades'),
    ('TRANSPORTATION', 'Transportation'), ('WASTEMGMT', 'Waste Management')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='businesses',)
    name = models.CharField('business name', max_length=100)
    city = models.CharField(max_length=100)
    price = models.CharField('selling price', max_length=100)
    early = models.DateField('beginning of availability')
    late = models.DateField('end of availability')
    state = models.CharField(
        choices=STATE_CHOICES,
        default='MT',
        max_length=100
    )
    industry = models.CharField(
        max_length=100,
        choices=INDUSTRY_CHOICES,
        default='TRADES'
    )
    last_update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Favorite(models.Model):
    veteran = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites',)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='favorites',)

from django.db import models
from viewflow.models import Process
from localflavor.us.models import USZipCodeField, USStateField
from django.contrib.auth.models import AbstractUser

# validating here in models rather than mess with CreateView in my View-Form process...

class User(AbstractUser):
    is_veteran = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location_zip = USZipCodeField()
    location_state = USStateField()
    profile_url = models.TextField(null=True, blank=True)
    org_name = models.CharField(max_length=100)
    org_url = models.TextField(null=True, blank=True)
    education = models.CharField(max_length=280)
    bio = models.CharField(max_length=280)
    last_update = models.DateField(auto_now=true)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

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
    veteran = models.ForeignKey(auth.User, on_delete=models.CASCADE, related_name='searches')
    name = models.CharField(max_length=100)
    early = models.DateField()
    late = models.DateField()
    state = models.CharField(
        choices=STATE_CHOICES,
        default='MT'
    )
    industry = models.CharField(
        max_length=2,
        choices=INDUSTRY_CHOICES,
        default='TRADES'
    )
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
    broker = models.ForeignKey(auth.User, on_delete=models.CASCADE, related_name='businesses')
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    early = models.DateField()
    late = models.DateField()
    state = models.CharField(
        choices=STATE_CHOICES,
        default='MT'
    )
    industry = models.CharField(
        max_length=2,
        choices=INDUSTRY_CHOICES,
        default='TRADES'
    )
    def __str__(self):
        return self.name

class Favorite(models.Model):
    veteran = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='favorites')
    business = models.ForeignKey(Business, related_name='favorites', on_delete=models.CASCADE)

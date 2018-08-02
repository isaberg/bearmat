from django.db import models
from viewflow.models import Process
from localflavor.us.models import USZipCodeField, USStateField
from django.contrib.auth.models import AbstractUser

# validating here rather than mess with CreateView in my View-Form process...
# from localflavor.us.forms import FRPhoneNumberField
# localflavor.us.models.USZipCodeField()
# localflavor.us.models.USStateField()

class User(AbstractUser):
    is_veteran = models.BooleanField(default=False)
    is_broker = models.BooleanField(default=False)

# structure...maybe just have a "Profile" that captures veteran/broker info?

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
    lastUpdated

class Search(models.Model):
    veteran = models.ForeignKey(User, on_delete=models.CASCADE, related_name='searches')
    early = models.



class Business(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    name:
city:
state:
Search (Record of Business Desired)
veteran: FOREIGNKEY of originator
go: (checkbox array of location/industry/$) nogo: (checkbox array of location/industry/$)
    industry: price: description:

class Veteran(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    # interests = models.ManyToManyField(Subject, related_name='interested_students')
    # This is what the vet model needs:
    # firstName: lastName: location: service: education:
    # bio: messages: profileURL:

class Broker(models.Model):
    # This is what the broker model needs:
    # firstName:
    # lastName: profileURL: organization: organizationURL: location:


# A one-to-one relationship is quite similar to a many-to-one relationship, except that it restricts two objects to having a unique relationship.
# An example of this would be a User and a Profile (which stores information about the user). No
# two users share the same profile. Let's look at this in Django. I won't bother to define the
# user model, as Django defines it for us. Do note, however, that Django suggests using
# django.contrib.auth.get_user_model() to import the user, so that's what we'll do.
# The profile model may be defined as follows:

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL) # Note that Django suggests getting the User from the settings for relationship definitions
#     fruit = models.CharField(max_length=50, help_text="Favorite Fruit")
#     facebook = models.CharField(max_length=100, help_text="Facebook Username")
#
#     def __unicode__(self):
#         return "".join(self.fruit, " ", self.facebook)

# class HelloWorldProcess(Process):
#     text = models.CharField(max_length=150)
#     approved = models.BooleanField(default=False)
#
# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     photo_url = models.TextField()
#     nationality = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Song(models.Model):
#     title = models.CharField(max_length=100)
#     album = models.CharField(max_length=100)
#     preview_url = models.TextField(null=True, blank=True)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
#
#     def __str__(self):
#         return self.title
#
#
# class Favorite(models.Model):
#     user = models.ForeignKey('auth.User', related_name='favorites', on_delete=models.CASCADE)
#     song = models.ForeignKey(Song, related_name='favorites', on_delete=models.CASCADE)

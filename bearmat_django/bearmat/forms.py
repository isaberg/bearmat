from django import forms
from .models import Profile, Search, Business, Favorite
from localflavor import generic
from localflavor.us.forms import USStateField, USZipCodeField
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import (User, Profile, Search, Business, Favorite)



# this handles all user signup - must distinguish between vets and brokers
class VeteranSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    @transaction.atomic
    def save (self, commit=True):
        user = super().save(commit=False)
        user.is_veteran = True
        if commit:
            user.save()
        return user

class BrokerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    @transaction.atomic
    def save (self, commit=True):
        user = super().save(commit=False)
        user.is_veteran = True
        if commit:
            user.save()
        return user

# this handles profile creation for veterans and brokers
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'location_zip', 'location_state', 'profile_url', 'org_name', 'org_url', 'education', 'bio')
    help_texts = {
        'location_zip': 'format example: #####',
        'location_state': 'format example: MT',
        'profile_url': 'copy/paste image source URL from image hosting provider',
        'org_name': 'name of your current organization, service, employer or school',
        'org_url': 'copy/paste URL of organization homepage',
        'education': 'brief summary of formal education and any honors',
        'bio': 'brief bio'
        }

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('user', 'name', 'early', 'late', 'state', 'industry')
        help_texts = {
            'name': 'brief description example: New England summer 2019, US Army infantry officer, experience in construction',
            'early': 'the earliest date to go full time: format 1/1/2020',
            'late': 'the latest date to go full time: format 1/1/2020',
            'state': 'pick the state or states your are willing to pursue entrepreneurship in',
            'industry': 'pick the industries you are most interested in',
            }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('user', 'name', 'city', 'price', 'early', 'late', 'state', 'industry')
    help_texts = {
        'name': 'name of business for sale',
        'city': 'city in which business is headquartered',
        'price': 'price and associated terms in brief',
        'early': 'the earliest date for sale: format 1/1/2020',
        'late': 'the latest date for sale: format 1/1/2020',
        'state': 'pick the state this business is located in',
        'industry': 'pick the industries most closely associated with this business',
        }

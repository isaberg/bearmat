from django import forms
from .models import broker, Veteran, Business, Search
from localflavor import generic
from localflavor.us.forms import USStateField, USZipCodeField
from django.db import transaction

# this handles all user signup - must distinguish between vets and brokers
class VeteranSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
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
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    @transaction.atomic
    def save (self, commit=True):
        user = super().save(commit=False)
        user.is_veteran = True
        if commit:
            user.save()
        return user

# this handles profile creation for veterans
# model this conditional off of
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (first_name, last_name, location_zip, location_state, profile_url, org_name, org_url, education, bio)

class SearchForm(forms.ModelForm):
    state = USStateField()
    zip = USZipCodeField()

    class Meta:
        model = Profile
        fields = ('', '')


## SAVE this, look at use of queryset and widget for future checkbox in "Search" creation...

# class StudentSignUpForm(UserCreationForm):
#     interests = forms.ModelMultipleChoiceField(
#         queryset=Subject.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True
#     )
#
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_student = True
#         user.save()
#         student = Student.objects.create(user=user)
#         student.interests.add(*self.cleaned_data.get('interests'))
#         return user

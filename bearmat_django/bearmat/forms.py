from django import forms
from .models import Brokerage, Veteran, Business, Search
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
    def save (self, commit=True):
        user = super().save(commit=False)
        user.is_veteran = True
        if commit:
            user.save()
        return user


## MUST use this approach:
#
# class TeacherSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_teacher = True
#         if commit:
#             user.save()
#         return user
#
#
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


# this handles profile creation for veterans
# model this conditional off of
class VeteranForm(forms.ModelForm):
    state = USStateField()
    zip = USZipCodeField()

    class Meta:
        model = Profile
        fields = ('', '')

## example for "student sign up" that I want to use for veteran profile forms
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


class BrokerageForm(forms.ModelForm):
    state = USStateField()
    zip = USZipCodeField()

    class Meta:
        model = Profile
        fields = ('', '')


#Another example below...how to use validator MyFormField()
# class ArticleForm(ModelForm):
#     headline = MyFormField(
#         max_length=200,
#         required=False,
#         help_text='Use puns liberally',
#     )
#
#     class Meta:
#         model = Article
#         fields = ['headline', 'content']


# Localflavor example below...use for US state / zip code validation

# forms.py
# from django import forms
# from localflavor.fr.forms import FRPhoneNumberField
#
# class MyForm(forms.Form):
#     my_french_phone_no = FRPhoneNumberField()


# class USStateField(Field):
#     """
#     A form field that validates its input is a U.S. state name or abbreviation.
#     It normalizes the input to the standard two-leter postal service
#     abbreviation for the given state.
#     """
#     default_error_messages = {
#         'invalid': _('Enter a U.S. state or territory.'),
#     }
#
#     def clean(self, value):
#         from .us_states import STATES_NORMALIZED
#         super(USStateField, self).clean(value)
#         if value in EMPTY_VALUES:
#             return ''
#         try:
#             value = value.strip().lower()
#         except AttributeError:
#             pass
#         else:
#             try:
#                 return STATES_NORMALIZED[value.strip().lower()]
#             except KeyError:
#                 pass
#         raise ValidationError(self.error_messages['invalid'])


# from django import forms
# from localflavor.fr.forms import FRPhoneNumberField
#
# class MyForm(forms.Form):
#     my_french_phone_no = FRPhoneNumberField()

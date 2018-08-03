from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from .decorators import veteran_required, broker_required
from .forms import VeteranSignUpForm, BrokerSignUpForm, ProfileForm, SearchForm, BusinessForm
from .models import Profile, Search, Business, Favorite
from django.contrib.auth.models import User
## Strategy: Use default authentication for user login at root/accounts/login etc
## Once authenticated / logged in, PROFILE creation happens
## Veterans should see a different veteran/profile versus broker/profile

def home(request):
    if request.user.is_authenticated:
        if request.user.is_veteran:
            return redirect('veteran_home')
        else:
            return redirect('broker_home')
    return render(request, 'bearmat/home.html')

def veteran_home(request):
    veterans = User.objects.filter(is_veteran=True)
    return render(request, 'bearmat/veteran_home.html', {'veterans': veterans})
    # challenge: change the above query to return Profile information related 1:1

def broker_home(request):
    brokers = User.objects.filter(is_broker=True)
    return render(request, 'bearmat/broker_home.html', {'brokers': brokers})
    # challenge: change the above query to return Profile information related 1:1

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

class VeteranSignUpView(CreateView):
    model = User
    form_class = VeteranSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'veteran'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class BrokerSignUpView(CreateView):
    model = User
    form_class = BrokerSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'veteran'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def profile_detail(request, pk):
    if request.user.is_authenticated:
        if request.user.is_veteran:
            user = User.objects.get(id=pk)
            profile = user.profile
            return render(request, 'bearmat/veteran_profile.html', {'profile': profile})
        else:
            user = User.objects.get(id=pk)
            profile = user.profile
            return render(request, 'bearmat/broker_profile.html', {'profile': profile})
    return render(request, 'bearmat/home.html')

@login_required
def profile_edit(request, pk):
    if request.user.is_veteran:
        profile = Profile.objects.get(id=pk)
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                profile = form.save()
                return redirect('profile_detail', pk=profile.pk)
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'bearmat/profile_form_veteran.html', {'form': form})
    else:
        profile = Profile.objects.get(id=pk)
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                profile = form.save()
                return redirect('profile_detail', pk=profile.pk)
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'bearmat/profile_form_broker.html', {'form': form})

@login_required
@veteran_required
def search_detail(request, pk):
    search = Search.objects.get(id=pk)
    return render(request, 'bearmat/search_detail.html', {'search': search})

@login_required
@veteran_required
def search_create(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            return redirect('search_detail', pk=search.pk)
    else:
        form = SearchForm()
    return render(request, 'bearmat/artist_form.html', {'form': form})

# @login_required
# def profile_detail(request):
#     profile = Profile.objects.get(id=pk)
#     return render(request, 'tunr/artist_detail.html', {'artist': artist})
#
# @login_required
# def profile_create(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             song = form.save()
#             return redirect('song_detail', pk=song.pk)
#     else:
#         form = SongForm()
#     return render(request, 'tunr/song_form.html', {'form': form})
#

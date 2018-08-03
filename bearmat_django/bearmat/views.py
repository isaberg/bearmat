from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from .decorators import veteran_required, broker_required
from .forms import VeteranSignUpForm, BrokerSignUpForm, ProfileForm, SearchForm, BusinessForm
from .models import Profile, Search, Business, Favorite
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

## Strategy: Use default authentication for user login at root/accounts/login etc
## Once authenticated / logged in, PROFILE creation happens
## Veterans should see a different veteran/profile versus broker/profile

def home(request):
    if request.user.is_authenticated:
        if request.user.is_veteran:
            veterans = User.objects.filter(is_veteran=True)
            return render(request, 'bearmat/veteran_home.html', {'veterans': veterans})
        else:
            brokers = User.objects.filter(is_broker=True)
            return render(request, 'bearmat/broker_home.html', {'brokers': brokers})
    return render(request, 'bearmat/home.html')

def mission(request):
    return render(request, 'bearmat/mission.html')

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
        kwargs['user_type'] = 'broker'
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
        profile = Profile.objects.get(user_id=pk)
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                profile = form.save()
                return redirect('profile_detail', pk=profile.pk)
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'bearmat/profile_form_veteran.html', {'form': form})
    else:
        profile = Profile.objects.get(user_id=pk)
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                profile = form.save()
                return redirect('profile_detail', pk=profile.pk)
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'bearmat/profile_form_broker.html', {'form': form})

@login_required
def profile_delete(request, pk):
    Profile.objects.get(id=pk).delete()
    return redirect('home')

@login_required
@veteran_required
def search_detail(request, pk):
    search = Search.objects.get(id=pk)
    return render(request, 'bearmat/search_detail.html', {'search': search})

@login_required
def search_list(request):
    searches = Search.objects.all()
    return render(request, 'bearmat/search_list.html', {'searches': searches})

@login_required
@veteran_required
def search_create(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.save()
            search.user_id = request.user
            return redirect('search_detail', pk=search.pk)
    else:
        form = SearchForm()
    return render(request, 'bearmat/search_form.html', {'form': form})

@login_required
@veteran_required
def search_edit(request, pk):
    search = Search.objects.get(user_id=pk)
    if request.method == "POST":
        form = SearchForm(request.POST, instance=search)
        if form.is_valid():
            search = form.save()
            search.user_id = request.user
            return redirect('search_detail', pk=search.pk)
    else:
        form = SearchForm(instance=search)
    return render(request, 'bearmat/search_form.html', {'form': form})

@login_required
@veteran_required
def search_delete(request, pk):
    Search.objects.get(id=pk).delete()
    return redirect('home')

@login_required
def business_detail(request, pk):
    business = Business.objects.get(id=pk)
    return render(request, 'bearmat/business_detail.html', {'business': business})

@login_required
def business_list(request):
    businesses = Business.objects.all()
    return render(request, 'bearmat/business_list.html', {'businesses': businesses})

@login_required
@broker_required
def business_create(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save()
            business.user_id = request.user
            return redirect('business_detail', pk=business.pk)
    else:
        form = BusinessForm()
    return render(request, 'bearmat/business_form.html', {'form': form})

@login_required
@broker_required
def business_edit(request, pk):
    business = Business.objects.get(user_id=pk)
    if request.method == "POST":
        form = BusinessForm(request.POST, instance=business)
        if form.is_valid():
            business = form.save()
            business.user_id = request.user
            return redirect('business_detail', pk=business.pk)
    else:
        form = BusinessForm(instance=business)
    return render(request, 'bearmat/business_form.html', {'form': form})

@login_required
@broker_required
def business_delete(request, pk):
    Business.objects.get(id=pk).delete()
    return redirect('home')

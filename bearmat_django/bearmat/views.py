from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from decorators import veteran_required, broker_required
from forms import SignUpForm
from models import Profile, Search, Business, Message
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
    return render(request, 'home.html')

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

class brokerSignUpView(CreateView):
    model = User
    form_class = brokerSignUpForm
    template_name = 'registration/signup_form.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'veteran'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def profile_detail(request):
    profile = Profile.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})


@login_required
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            song = form.save()
            return redirect('song_detail', pk=song.pk)
    else:
        form = SongForm()
    return render(request, 'tunr/song_form.html', {'form': form})



# # Create your views here.
#
# def artist_detail(request, pk):
#     artist = Artist.objects.get(id=pk)
#     return render(request, 'tunr/artist_detail.html', {'artist': artist})
#
# Example using custom decorators (for creating business and creating search)
# @login_required
# @student_required  # <-- here!
# def take_quiz(request, pk):
#     quiz = get_object_or_404(Quiz, pk=pk)
#     student = request.user.student
#
#     # body of the view...
#
#     return render(request, 'classroom/students/take_quiz_form.html', {
#         'quiz': quiz,
#         'question': question,
#         'form': form,
#         'progress': progress
#     })

# EXAMPLE from CLASSROOM
#
#
# class StudentSignUpView(CreateView):
#     model = User
#     form_class = StudentSignUpForm
#     template_name = 'registration/signup_form.html'
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('students:quiz_list')

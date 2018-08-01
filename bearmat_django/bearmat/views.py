from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from decorators import veteran_required, brokerage_required
from forms import SignUpForm
from models import User, Profile, Search, Business, Message

## Strategy: Use default authentication for user login at root/accounts/login etc
## Once authenticated / logged in, PROFILE creation happens

class VeteranProfileView(CreateView):
    model = Profile
    form_class = VeteranForm
    template_name = 'registration/profile_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'veteran'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')


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

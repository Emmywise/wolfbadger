from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.shortcuts import redirect



@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = User
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        return self.request.user


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['name', 'address', 'phone_number']
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Get the user's profile or create it if it doesn't exist
        user_profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        return user_profile


#delete function
@login_required
def delete_profile(request):
    user_profile = request.user.userprofile
    user_profile.delete()
    return redirect('home')
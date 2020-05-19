from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from apps.userprofile.models import Profile
from django.contrib.auth import authenticate, login
from apps.common.models import Contact

class HomeView(TemplateView):
    template_name = "common/home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "common/dashboard.html"
    login_url = reverse_lazy('home')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_url = request.GET.get('next', 'home')
                return HttpResponseRedirect('dashboard')
            else:
                return HttpResponse("Inactive user.")

        return render(request, "dashboard.html")

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = "common/signup.html"

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "common/profile.html"

class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = "common/profile-update.html"

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



def contact(request):
    if request.method == "POST":
        firstname_r = request.POST.get('firstname')
        lastname_r = request.POST.get('lastname')
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')

        c = Contact(firstname=firstname_r, lastname=lastname_r, email=email_r, subject=subject_r)
        c.save()

        return render(request, 'common/contact.html')
    else:
        return render(request, 'common/contact.html')
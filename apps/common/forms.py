from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.userprofile.models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=255, help_text="Enter a valid email address")

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",

        ]

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]

class ProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=11, required=True)

    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "birth_date",
            "length",
            "shoulder_back",
            "chest",
            "stomach_fit",
            "sleeve",
            "bicep_arm",
            "cuff",
            "neck",
            "head",
            "length_trouser",
            "thigh",
            "waist",
            "ankle",
            "knee",
            "calf",
            "profile_image",
        ]
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .models import CandidateProfile, User,Company

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields=(
            "first_name",
            "last_name",
            "username",
            "email",
            "role",
            "password1",
            "password2",
        )

class LoginForm(forms.Form):

    username = forms.CharField(
        max_length=150
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )


class CandidateProfileForm(forms.ModelForm):

    class Meta:
        model = CandidateProfile

        fields = [
            "phone",
            "location",
            "bio",
            "skills",
            "education",
            "experience",
            "resume",
            "profile_image",
        ]

        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Tell recruiters about yourself..."
                }
            ),

            "skills": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Python, Django, SQL, C++..."
                }
            ),
        }



class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company

        fields = [
            "name",
            "description",
            "website",
            "location",
            "logo",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Tell candidates about your company..."
                }
            ),
        }
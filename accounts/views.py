from django.shortcuts import render,redirect
from .forms import SignUpForm ,LoginForm
from .models import CandidateProfile, Company
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .forms import (CandidateProfileForm, LoginForm,SignUpForm,CompanyForm,)

from dashboard.decorators import role_required


# Create your views here.
def signup(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)   

        if form.is_valid():
            user=form.save()

            if user.role == "CANDIDATE":
                CandidateProfile.objects.create(user=user)
                return redirect("candidate_dashboard")
            else:
                Company.objects.create(
                    user=user,
                    name=f"{user.username}'s Company"
                )
                return redirect("recruiter_dashboard")
    else:
        form = SignUpForm()

    return render(request, "accounts/signup.html", {"form": form})

def user_login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)

                if user.role == "CANDIDATE":
                    return redirect("candidate_dashboard")

                return redirect("recruiter_dashboard")

            form.add_error(
                None,
                "Invalid username or password."
            )

    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )

def user_logout(request):

    logout(request)

    return redirect("login")


# user can update his profile 
@login_required
def candidate_profile(request):

    profile = request.user.candidate_profile

    if request.method == "POST":

        form = CandidateProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():

            form.save()

            return redirect("candidate_profile")

    else:

        form = CandidateProfileForm(
            instance=profile
        )

    return render(
        request,
        "accounts/candidate_profile.html",
        {"form": form}
    )


@login_required
@role_required("RECRUITER")
def company_profile(request):

    company = request.user.company

    if request.method == "POST":

        form = CompanyForm(
            request.POST,
            request.FILES,
            instance=company
        )

        if form.is_valid():

            form.save()

            return redirect("company_profile")

    else:

        form = CompanyForm(
            instance=company
        )

    return render(
        request,
        "accounts/company_profile.html",
        {"form": form}
    )

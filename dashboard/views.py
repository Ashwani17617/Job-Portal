from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from functools import wraps
from .decorators import role_required

# Create your views here.
@login_required
@role_required("CANDIDATE")
def candidate_dashboard(request):
    return render(request, "dashboard/candidate_dashboard.html")

@login_required
@role_required("RECRUITER")
def recruiter_dashboard(request):
    return render(request, "dashboard/recruiter_dashboard.html")    
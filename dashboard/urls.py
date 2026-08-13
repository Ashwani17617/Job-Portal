from django.urls import path

from . import views


urlpatterns = [
    path("candidate/", views.candidate_dashboard, name="candidate_dashboard"),
    path("recruiter/", views.recruiter_dashboard, name="recruiter_dashboard"),
]
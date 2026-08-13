from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "jobs/<int:job_id>/",
        views.job_detail,
        name="job_detail"
    ),

    path(
        "jobs/<int:job_id>/apply/",
        views.apply_job,
        name="apply_job"
    ),
    path(
    "my-applications/",
    views.candidate_applications,
    name="candidate_applications"
    ),

    path(
    "recruiter/jobs/create/",
    views.create_job,
    name="create_job"
    ),

    path(
    "recruiter/jobs/",
    views.recruiter_jobs,
    name="recruiter_jobs"
    ),

    path(
    "recruiter/jobs/<int:job_id>/applicants/",
    views.job_applicants,
    name="job_applicants"
    ),

    path(
    "recruiter/applications/<int:application_id>/status/",
    views.update_application_status,
    name="update_application_status"
),
]
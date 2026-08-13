from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required

from dashboard.decorators import role_required



from .models import Job
from .forms import ApplicationForm, ApplicationStatusForm, JobForm
from .models import Application


def home(request):

    jobs = Job.objects.filter(
        is_active=True
    ).order_by("-created_at")[:6]

    return render(
        request,
        "jobs/home.html",
        {"jobs": jobs}
    )

def job_detail(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )


    return render(
        request,
        "jobs/job_detail.html",
        {"job": job}
    )
    
@login_required
@role_required("CANDIDATE")
def apply_job(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id,
        is_active=True
    )

    candidate = request.user.candidate_profile

    if Application.objects.filter(
        candidate=candidate,
        job=job
    ).exists():

        return render(
            request,
            "jobs/already_applied.html",
            {"job": job}
        )

    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save(commit=False)

            application.candidate = candidate
            application.job = job

            application.save()

            return redirect(
                "candidate_applications"
            )

    else:
        form = ApplicationForm()

    return render(
        request,
        "jobs/apply.html",
        {
            "form": form,
            "job": job
        }
    )

@login_required
@role_required("CANDIDATE")
def candidate_applications(request):

    applications = (
        request.user.candidate_profile
        .applications
        .select_related("job", "job__company")
        .order_by("-applied_at")
    )

    return render(
        request,
        "jobs/candidate_applications.html",
        {"applications": applications}
    )




# recuiter dashboard views
@login_required
@role_required("RECRUITER")
def create_job(request):

    company = request.user.company

    if request.method == "POST":

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.company = company

            job.save()

            return redirect("recruiter_jobs")

    else:
        form = JobForm()

    return render(
        request,
        "jobs/create_job.html",
        {"form": form}
    )



@login_required
@role_required("RECRUITER")
def recruiter_jobs(request):

    jobs = (
        request.user.company
        .jobs
        .order_by("-created_at")
    )

    return render(
        request,
        "jobs/recruiter_jobs.html",
        {"jobs": jobs}
    )



@login_required
@role_required("RECRUITER")
def job_applicants(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id,
        company=request.user.company
    )

    applications = (
        job.applications
        .select_related("candidate", "candidate__user")
        .order_by("-applied_at")
    )

    return render(
        request,
        "jobs/job_applicants.html",
        {
            "job": job,
            "applications": applications
        }
    )


@login_required
@role_required("RECRUITER")
def update_application_status(request, application_id):

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company=request.user.company
    )

    if request.method == "POST":

        form = ApplicationStatusForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            form.save()

            return redirect(
                "job_applicants",
                job_id=application.job.id
            )

    else:

        form = ApplicationStatusForm(
            instance=application
        )

    return render(
        request,
        "jobs/update_application_status.html",
        {
            "form": form,
            "application": application
        }
    )
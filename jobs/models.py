from django.db import models
from accounts.models import Company


class Job(models.Model):

    class JobType(models.TextChoices):
        FULL_TIME = "FULL_TIME", "Full Time"
        PART_TIME = "PART_TIME", "Part Time"
        INTERNSHIP = "INTERNSHIP", "Internship"
        CONTRACT = "CONTRACT", "Contract"

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    requirements = models.TextField()

    location = models.CharField(max_length=100)

    job_type = models.CharField(
        max_length=20,
        choices=JobType.choices,
        default=JobType.FULL_TIME
    )

    salary_min = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    salary_max = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    experience_required = models.CharField(
        max_length=100,
        blank=True
    )

    skills = models.TextField()

    deadline = models.DateField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Application(models.Model):

    class Status(models.TextChoices):
        APPLIED = "APPLIED", "Applied"
        SHORTLISTED = "SHORTLISTED", "Shortlisted"
        REJECTED = "REJECTED", "Rejected"
        SELECTED = "SELECTED", "Selected"

    candidate = models.ForeignKey(
        "accounts.CandidateProfile",
        on_delete=models.CASCADE,
        related_name="applications"
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    resume = models.FileField(
        upload_to="application_resumes/",
        blank=True,
        null=True
    )

    cover_letter = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.APPLIED
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints=[models.UniqueConstraint(
            fields=['candidate', 'job'],
            name="unique_candidate_job_application")
            ]

    def __str__(self):
        return f"{self.candidate.user.username} - {self.job.title}"
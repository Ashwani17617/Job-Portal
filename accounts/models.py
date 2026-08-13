from django.db import models
from django.contrib.auth.models import AbstractUser


class UserRole(models.TextChoices):
    CANDIDATE = "CANDIDATE", "Candidate"
    RECRUITER = "RECRUITER", "Recruiter"


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CANDIDATE
    )

class CandidateProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='candidate_profile')

    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    education = models.CharField(max_length=200, blank=True)
    experience = models.CharField(max_length=100, blank=True)


    resume =models.FileField(upload_to='resumes/', blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username



class Company(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="company"
    )

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    logo = models.ImageField(
        upload_to="company_logos/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


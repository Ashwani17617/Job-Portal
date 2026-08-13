from django import forms
from .models import Application, Job


class ApplicationForm(forms.ModelForm):
    class Meta:
        model =Application
        fields = [
            "resume",
            "cover_letter",
        ]

        widgets = {
            "cover_letter": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Write your cover letter..."
                }
            ),
        }

# this is from recruiter side form 
class JobForm(forms.ModelForm):

    class Meta:
        model = Job

        fields = [
            "title",
            "description",
            "requirements",
            "location",
            "job_type",
            "salary_min",
            "salary_max",
            "experience_required",
            "skills",
            "deadline",
            "is_active",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 5}
            ),

            "requirements": forms.Textarea(
                attrs={"rows": 5}
            ),

            "skills": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Python, Django, SQL, REST API"
                }
            ),

            "deadline": forms.DateInput(
                attrs={"type": "date"}
            ),
        }


# it tell the status of job when action is taken by recruiter on candidate application
class ApplicationStatusForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ["status"]




from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, CandidateProfile, Company

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Job Portal Information", {
            "fields": ("role",),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Job Portal Information", {
            "fields": ("role",),
        }),
    )

admin.site.register(CandidateProfile)
admin.site.register(Company)

# Register your models here.

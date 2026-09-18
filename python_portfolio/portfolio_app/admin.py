from django.contrib import admin

from .models import (
    Certification,
    ContactMessage,
    Education,
    Experience,
    Project,
    Service,
    SiteProfile,
    Skill,
)


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Identity",
            {"fields": ("name", "title", "tagline", "availability")},
        ),
        ("About", {"fields": ("about_intro", "about_details")}),
        (
            "Contact",
            {"fields": ("email", "phone", "location", "github_url", "linkedin_url", "resume_file")},
        ),
        (
            "Statistics",
            {
                "fields": (
                    "years_experience",
                    "projects_completed",
                    "technologies_count",
                    "github_contributions",
                    "github_repos",
                    "github_stars",
                )
            },
        ),
        ("SEO", {"fields": ("meta_description",)}),
    )

    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "display_order")
    list_filter = ("category",)
    list_editable = ("proficiency", "display_order")
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "is_current", "display_order")
    list_filter = ("is_current",)
    search_fields = ("title", "company")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "is_featured", "display_order")
    list_filter = ("is_featured",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "summary")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "display_order")
    search_fields = ("degree", "institution")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "issue_date", "display_order")
    search_fields = ("name", "issuer")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "display_order")
    search_fields = ("title",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at", "ip_address")
    list_editable = ("is_read",)

    def has_add_permission(self, request):
        return False

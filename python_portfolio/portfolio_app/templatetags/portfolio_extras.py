from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def resume_url(profile):
    if profile and profile.resume_file:
        return profile.resume_file.url
    return static("resume/YOUR_RESUME.pdf")

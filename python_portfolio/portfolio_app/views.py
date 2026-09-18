from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from .forms import ContactForm
from .models import (
    Certification,
    Education,
    Experience,
    Project,
    Service,
    Skill,
)


def _client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def _portfolio_context(request, form=None):
    skills = Skill.objects.all()
    grouped_skills = []
    for value, label in Skill.Category.choices:
        category_skills = [skill for skill in skills if skill.category == value]
        if category_skills:
            grouped_skills.append({"key": value, "label": label, "skills": category_skills})

    return {
        "form": form or ContactForm(initial={"form_started": str(int(timezone.now().timestamp()))}),
        "skills_grouped": grouped_skills,
        "experiences": Experience.objects.all(),
        "projects": Project.objects.all(),
        "education_items": Education.objects.all(),
        "certifications": Certification.objects.all(),
        "services": Service.objects.all(),
    }


@require_http_methods(["GET", "POST"])
def home(request):
    if request.method == "POST":
        last_submit = request.session.get("contact_submitted_at")
        now_ts = timezone.now().timestamp()
        if last_submit and now_ts - float(last_submit) < 20:
            messages.error(request, "Please wait a moment before sending another message.")
            return redirect(f"{reverse('home')}#contact")

        form = ContactForm(request.POST)
        started = request.POST.get("form_started", "")
        too_fast = False
        if started.isdigit() and now_ts - int(started) < 3:
            too_fast = True

        if form.is_valid() and not too_fast:
            contact = form.save(commit=False)
            contact.ip_address = _client_ip(request)
            contact.save()
            request.session["contact_submitted_at"] = str(now_ts)
            messages.success(request, "Message received. I will get back to you soon.")
            return redirect(f"{reverse('home')}#contact")

        if too_fast:
            messages.error(request, "Please take a second and try again.")
        else:
            messages.error(request, "Please correct the errors in the form.")
        context = _portfolio_context(request, form=form)
        return render(request, "portfolio_app/index.html", context)

    return render(request, "portfolio_app/index.html", _portfolio_context(request))


def robots_txt(request):
    sitemap_url = request.build_absolute_uri(reverse("django.contrib.sitemaps.views.sitemap"))
    content = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            "Disallow: /admin/",
            f"Sitemap: {sitemap_url}",
            "",
        ]
    )
    return HttpResponse(content, content_type="text/plain")

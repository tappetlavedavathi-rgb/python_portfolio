from django.db import models
from django.utils import timezone


class SiteProfile(models.Model):
    name = models.CharField(max_length=120, default="[YOUR NAME]")
    title = models.CharField(max_length=160, default="Python Developer")
    tagline = models.CharField(
        max_length=255,
        default="I build reliable backend systems, REST APIs, and clean Django applications.",
    )
    about_intro = models.TextField(
        default=(
            "I am a Python/Django developer focused on backend architecture, "
            "REST APIs, and production-ready web applications. I care about "
            "clear models, maintainable views, and interfaces that feel considered."
        )
    )
    about_details = models.TextField(
        default=(
            "My work spans authentication, CRUD workflows, database design, and "
            "API integrations. I write readable Python, structure Django apps "
            "for long-term maintenance, and ship with deployment in mind."
        )
    )
    email = models.EmailField(default="[YOUR EMAIL]")
    phone = models.CharField(max_length=80, default="[YOUR PHONE]")
    location = models.CharField(max_length=120, default="[YOUR LOCATION]")
    github_url = models.URLField(default="https://github.com/[YOUR GITHUB]")
    linkedin_url = models.URLField(default="https://linkedin.com/in/[YOUR LINKEDIN]")
    resume_file = models.FileField(upload_to="resume/", blank=True)
    years_experience = models.PositiveIntegerField(default=3)
    projects_completed = models.PositiveIntegerField(default=12)
    technologies_count = models.PositiveIntegerField(default=18)
    github_contributions = models.PositiveIntegerField(default=800)
    github_repos = models.PositiveIntegerField(default=24)
    github_stars = models.PositiveIntegerField(default=48)
    availability = models.CharField(
        max_length=120,
        default="Open to full-time roles, freelance, and contract work",
    )
    meta_description = models.CharField(
        max_length=220,
        default=(
            "Python & Django developer portfolio — backend systems, REST APIs, "
            "and production web applications."
        ),
    )

    class Meta:
        verbose_name = "Site profile"
        verbose_name_plural = "Site profile"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.name


class Skill(models.Model):
    class Category(models.TextChoices):
        PROGRAMMING = "programming", "Programming"
        BACKEND = "backend", "Backend"
        DATABASE = "database", "Database"
        TOOLS = "tools", "Tools"
        DEPLOYMENT = "deployment", "Deployment"

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=32, choices=Category.choices)
    proficiency = models.PositiveSmallIntegerField(default=80)
    icon = models.CharField(max_length=40, blank=True, help_text="Optional icon keyword")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["category", "display_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Experience(models.Model):
    title = models.CharField(max_length=140)
    company = models.CharField(max_length=140)
    location = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    responsibilities = models.TextField(help_text="One responsibility per line")
    technologies = models.CharField(max_length=255, help_text="Comma-separated")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-start_date"]

    def __str__(self):
        return f"{self.title} — {self.company}"

    def responsibility_list(self):
        return [line.strip() for line in self.responsibilities.splitlines() if line.strip()]

    def technology_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]

    def period_label(self):
        start = self.start_date.strftime("%b %Y")
        if self.is_current or not self.end_date:
            return f"{start} — Present"
        return f"{start} — {self.end_date.strftime('%b %Y')}"


class Project(models.Model):
    name = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=220)
    description = models.TextField()
    features = models.TextField(help_text="One feature per line")
    technologies = models.CharField(max_length=255, help_text="Comma-separated")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    accent = models.CharField(max_length=20, default="#3ee0b1")
    is_featured = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name

    def feature_list(self):
        return [line.strip() for line in self.features.splitlines() if line.strip()]

    def technology_list(self):
        return [item.strip() for item in self.technologies.split(",") if item.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=160)
    institution = models.CharField(max_length=160)
    location = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-start_date"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} — {self.institution}"

    def period_label(self):
        start = self.start_date.strftime("%Y")
        if not self.end_date:
            return f"{start} — Present"
        return f"{start} — {self.end_date.strftime('%Y')}"


class Certification(models.Model):
    name = models.CharField(max_length=180)
    issuer = models.CharField(max_length=140)
    issue_date = models.DateField()
    credential_url = models.URLField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "-issue_date"]

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField()
    icon = models.CharField(max_length=40, default="code")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.subject} — {self.name}"

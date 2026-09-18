from datetime import date

from .models import (
    Certification,
    Education,
    Experience,
    Project,
    Service,
    SiteProfile,
    Skill,
)


def seed_portfolio_content():
    SiteProfile.load()

    if not Skill.objects.exists():
        skills = [
            ("Python", Skill.Category.PROGRAMMING, 95, 1),
            ("JavaScript", Skill.Category.PROGRAMMING, 80, 2),
            ("HTML", Skill.Category.PROGRAMMING, 90, 3),
            ("CSS", Skill.Category.PROGRAMMING, 88, 4),
            ("SQL", Skill.Category.PROGRAMMING, 86, 5),
            ("Django", Skill.Category.BACKEND, 94, 1),
            ("Django REST Framework", Skill.Category.BACKEND, 90, 2),
            ("REST APIs", Skill.Category.BACKEND, 92, 3),
            ("Authentication", Skill.Category.BACKEND, 88, 4),
            ("CRUD", Skill.Category.BACKEND, 93, 5),
            ("API Integration", Skill.Category.BACKEND, 85, 6),
            ("PostgreSQL", Skill.Category.DATABASE, 88, 1),
            ("MySQL", Skill.Category.DATABASE, 80, 2),
            ("SQLite", Skill.Category.DATABASE, 90, 3),
            ("Git", Skill.Category.TOOLS, 90, 1),
            ("GitHub", Skill.Category.TOOLS, 90, 2),
            ("VS Code", Skill.Category.TOOLS, 92, 3),
            ("Postman", Skill.Category.TOOLS, 86, 4),
            ("Docker", Skill.Category.TOOLS, 78, 5),
            ("Render", Skill.Category.DEPLOYMENT, 82, 1),
            ("GitHub", Skill.Category.DEPLOYMENT, 88, 2),
            ("Linux", Skill.Category.DEPLOYMENT, 80, 3),
        ]
        Skill.objects.bulk_create(
            [
                Skill(name=name, category=category, proficiency=proficiency, display_order=order)
                for name, category, proficiency, order in skills
            ]
        )

    if not Experience.objects.exists():
        Experience.objects.bulk_create(
            [
                Experience(
                    title="Python / Django Developer",
                    company="[COMPANY NAME]",
                    location="[YOUR LOCATION]",
                    start_date=date(2023, 1, 1),
                    is_current=True,
                    responsibilities="\n".join(
                        [
                            "Designed and shipped Django applications with clean models, views, and admin workflows.",
                            "Built REST APIs with authentication, permissions, and documented endpoints.",
                            "Modeled relational data in PostgreSQL and SQLite with practical query patterns.",
                            "Collaborated on frontend templates, forms, and production deployments.",
                        ]
                    ),
                    technologies="Python, Django, DRF, PostgreSQL, Git, Render",
                    display_order=1,
                ),
                Experience(
                    title="Backend Developer",
                    company="[PREVIOUS COMPANY]",
                    location="[YOUR LOCATION]",
                    start_date=date(2021, 6, 1),
                    end_date=date(2022, 12, 1),
                    is_current=False,
                    responsibilities="\n".join(
                        [
                            "Implemented CRUD modules, user auth, and admin tooling for internal products.",
                            "Integrated third-party APIs and improved error handling around external services.",
                            "Wrote maintainable Python with tests, reviews, and clear pull request descriptions.",
                        ]
                    ),
                    technologies="Python, Django, MySQL, JavaScript, Postman",
                    display_order=2,
                ),
            ]
        )

    if not Project.objects.exists():
        Project.objects.bulk_create(
            [
                Project(
                    name="Django E-Commerce Platform",
                    slug="django-ecommerce-platform",
                    summary="A full-stack storefront with catalog, cart, orders, and an admin dashboard.",
                    description=(
                        "A Django e-commerce application covering catalog management, authenticated "
                        "checkout flows, and operational tooling for orders."
                    ),
                    features="\n".join(
                        [
                            "User authentication",
                            "Product management",
                            "Shopping cart",
                            "Orders",
                            "Admin dashboard",
                            "Payment integration placeholder",
                        ]
                    ),
                    technologies="Python, Django, PostgreSQL, JavaScript",
                    github_url="https://github.com/[YOUR GITHUB]/django-ecommerce",
                    live_url="https://example.com",
                    accent="#3ee0b1",
                    display_order=1,
                ),
                Project(
                    name="Task Management API",
                    slug="task-management-api",
                    summary="A permission-aware REST API for teams to create, assign, and track work.",
                    description=(
                        "A Django REST Framework service with JWT authentication, role-aware access, "
                        "and documented CRUD endpoints."
                    ),
                    features="\n".join(
                        [
                            "JWT authentication",
                            "CRUD APIs",
                            "User permissions",
                            "API documentation",
                        ]
                    ),
                    technologies="Python, Django REST Framework, PostgreSQL",
                    github_url="https://github.com/[YOUR GITHUB]/task-management-api",
                    live_url="https://example.com",
                    accent="#7c6cff",
                    display_order=2,
                ),
                Project(
                    name="Personal Expense Tracker",
                    slug="personal-expense-tracker",
                    summary="A private finance dashboard for categories, reports, and monthly insights.",
                    description=(
                        "A Django app for tracking spending by category with authentication, "
                        "summaries, and a lightweight dashboard."
                    ),
                    features="\n".join(
                        [
                            "Expense tracking",
                            "Categories",
                            "Reports",
                            "Dashboard",
                            "Authentication",
                        ]
                    ),
                    technologies="Python, Django, SQLite, JavaScript",
                    github_url="https://github.com/[YOUR GITHUB]/expense-tracker",
                    live_url="https://example.com",
                    accent="#f0b45a",
                    display_order=3,
                ),
            ]
        )

    if not Education.objects.exists():
        Education.objects.create(
            degree="[YOUR DEGREE]",
            institution="[YOUR UNIVERSITY]",
            location="[YOUR LOCATION]",
            start_date=date(2018, 6, 1),
            end_date=date(2022, 5, 1),
            description="Computer science coursework with emphasis on software engineering and databases.",
            display_order=1,
        )

    if not Certification.objects.exists():
        Certification.objects.bulk_create(
            [
                Certification(
                    name="[CERTIFICATION NAME]",
                    issuer="[ISSUER]",
                    issue_date=date(2024, 3, 1),
                    credential_url="https://example.com",
                    display_order=1,
                ),
                Certification(
                    name="Django for APIs",
                    issuer="[ISSUER]",
                    issue_date=date(2023, 11, 1),
                    credential_url="https://example.com",
                    display_order=2,
                ),
            ]
        )

    if not Service.objects.exists():
        Service.objects.bulk_create(
            [
                Service(
                    title="Django Web Applications",
                    description="Full Django products with auth, admin, templates, and production-ready settings.",
                    icon="layers",
                    display_order=1,
                ),
                Service(
                    title="REST API Development",
                    description="DRF APIs with authentication, permissions, pagination, and clean serializers.",
                    icon="api",
                    display_order=2,
                ),
                Service(
                    title="Database Design",
                    description="Practical schema design, migrations, and query work for PostgreSQL, MySQL, and SQLite.",
                    icon="database",
                    display_order=3,
                ),
                Service(
                    title="Deployment & Maintenance",
                    description="Render/Linux deployments, static files, environment config, and ongoing fixes.",
                    icon="cloud",
                    display_order=4,
                ),
            ]
        )

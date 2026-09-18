from django.test import TestCase
from django.urls import reverse

from portfolio_app.models import ContactMessage, SiteProfile


class PortfolioViewTests(TestCase):
    def test_home_renders(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        profile = SiteProfile.load()
        self.assertContains(response, profile.name)

    def test_robots_and_sitemap(self):
        self.assertEqual(self.client.get("/robots.txt").status_code, 200)
        self.assertEqual(self.client.get("/sitemap.xml").status_code, 200)

    def test_contact_form_saves_message(self):
        response = self.client.post(
            reverse("home"),
            {
                "name": "Alex Recruiter",
                "email": "alex@example.com",
                "subject": "Role inquiry",
                "message": "We would like to discuss a Django backend role.",
                "website": "",
                "form_started": "1",
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_form_rejects_honeypot(self):
        response = self.client.post(
            reverse("home"),
            {
                "name": "Bot",
                "email": "bot@example.com",
                "subject": "Spam subject",
                "message": "This is definitely a spam message.",
                "website": "https://spam.example",
                "form_started": "1",
            },
        )
        self.assertEqual(ContactMessage.objects.count(), 0)
        self.assertEqual(response.status_code, 200)

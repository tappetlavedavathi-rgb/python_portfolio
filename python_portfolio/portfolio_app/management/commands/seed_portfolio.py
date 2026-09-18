from django.core.management.base import BaseCommand

from portfolio_app.seed import seed_portfolio_content


class Command(BaseCommand):
    help = "Load placeholder portfolio content if the database is empty."

    def handle(self, *args, **options):
        seed_portfolio_content()
        self.stdout.write(self.style.SUCCESS("Portfolio content is ready."))

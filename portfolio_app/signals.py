from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .seed import seed_portfolio_content


@receiver(post_migrate)
def populate_default_content(sender, **kwargs):
    if sender.name != "portfolio_app":
        return
    seed_portfolio_content()

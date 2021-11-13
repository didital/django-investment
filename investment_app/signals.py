from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import InvestmentType, Transaction

@receiver(post_save, sender=Transaction)
def update_investment_type (sender, instance, created, **kwargs):
    pass
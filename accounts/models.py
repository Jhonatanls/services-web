from django.db import models
from django.contrib.auth.models import User
from aiservices.models import IAService
from django.db.models.signals import post_save


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    services = models.ManyToManyField(IAService)

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['-id']

    def __str__(self):
        return str(self.user)

def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

def save_user_account(sender, instance, **kwargs):
    instance.account.save()

post_save.connect(create_user_account, sender=User)
post_save.connect(save_user_account, sender=User)



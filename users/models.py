from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()


class Profile(models.Model):
    """
    Модель товара
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(
        blank=True, verbose_name='День рождения', default=None, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Дополнительное поле'
        verbose_name_plural = 'Дополнительное поля'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs) -> None:
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

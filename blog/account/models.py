from turtle import width
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
# from 
# from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    profile_image = models.ImageField(
        verbose_name='Картинка профиля',
        upload_to="photos/%Y/%m/%d",
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата рождения"
    )

    def __str__(self) -> str:
        return f'Профиль {self.user.username}'

    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"profile_id": self.pk})

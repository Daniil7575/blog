from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    profile_image = models.ImageField(
        verbose_name='Картинка профиля',
        upload_to="users/%Y/%m/%d",
        blank=True
    )

    date_of_birt = models.DateTimeField(
        blank=True,
        verbose_name="Дата рождения"
    )

    def __str__(self) -> str:
        return f'Профиль {self.user.username}'

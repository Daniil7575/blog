from django.db import models
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Автор",
        related_name="posts",
        
    )

    title = models.CharField(verbose_name="Заголовок", max_length=200)

    slug = models.SlugField(max_length=200, unique_for_date='published')

    body = models.TextField(verbose_name="Тело поста")

    published = models.DateTimeField(
        verbose_name="Дата и время публикации", 
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name="Дата и время последнего изменения",
        auto_now=True,
    )

    rating = models.IntegerField(
        verbose_name='Рейтинг',
        default=0
    )

    # rated_by??? = [???]

    class Meta:
        ordering = ['-published']

    def __str__(self) -> str:
        return self.slug

    def get_absolute_url(self):
        kwargs = {
            'year': self.published.year,
            'month': self.published.month,
            'day': self.published.day,
            'post': self.slug
        }
        return reverse("post_detail", kwargs=kwargs)
    

class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    name = models.CharField(max_length=150)

    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self) -> str:
        return f'Комментарий {self.name} к посту {self.post}'

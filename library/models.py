from django.db import models


class Book(models.Model):
    GENRE_CHOICE = (
        ('Ужасы', 'Ужасы'),
        ('Фантастика', 'Фантастика'),
        ('Комедия', 'Комедия'),
        ('Драма', 'Драма'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='Изобрвжение', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ценв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100, verbose_name='Жанр')
    email = models.EmailField(verbose_name='Почта')
    author = models.CharField(max_length=100, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
from django.db import models

class Book(models.Model):
    GENRE_CHOICE = (
        ('Ужасы', 'Ужасы'),
        ('Фантастика', 'Фантастика'),
        ('Комедия', 'Комедия'),
        ('Драма', 'Драма'),
        ('Приключение', 'Приключение'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='Изображение', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100, verbose_name='Жанр')
    email = models.EmailField(verbose_name='Почта')
    author = models.CharField(max_length=100, verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_genre_display(self):
        return dict(self.GENRE_CHOICE).get(self.genre, self.genre)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Review(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    comment = models.TextField(verbose_name='Комментарий')
    stars = models.CharField(choices=STARS, max_length=10, verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

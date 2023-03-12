from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class PriceModel(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    duration = models.CharField(max_length=20, verbose_name='Продолжительность')
    quantity = models.CharField(max_length=20, verbose_name='Количество фото')
    note = models.CharField(max_length=40, verbose_name='Примечание')
    desc = models.TextField(null=True, verbose_name="Подробное описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'

class FeedbackModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Автор')
    content = models.CharField(max_length=255, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/%Y/%m", verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class BlogModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Содержание")
    photo = models.ImageField(upload_to="photos/%Y/%m", verbose_name="Фото для карточки")
    photo_big = models.ImageField(upload_to="photos_big/%Y/%m", verbose_name="Фото большое")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория  ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['time_create', 'title']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class PortfolioModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name="Slug")
    col_1_1 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка1 №1')
    col_1_2 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка1 №2')
    col_1_3 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка1 №3')
    col_1_4 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка1 №4')
    col_1_5 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка1 №5')
    col_1_6 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", null=True, verbose_name='колонка1 №6')
    col_1_7 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", null=True, verbose_name='колонка1 №7')
    col_2_1 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка2 №1')
    col_2_2 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка2 №2')
    col_2_3 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка2 №3')
    col_2_4 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка2 №4')
    col_2_5 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка2 №5')
    col_2_6 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", null=True, verbose_name='колонка2 №6')
    col_2_7 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", null=True, verbose_name='колонка2 №7')
    col_3_1 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка3 №1')
    col_3_2 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка3 №2')
    col_3_3 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка3 №3')
    col_3_4 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка3 №4')
    col_3_5 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка3 №5')
    col_3_6 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", null=True, verbose_name='колонка3 №6')
    col_3_7 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", null=True, verbose_name='колонка3 №7')
    col_4_1 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка4 №1')
    col_4_2 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка4 №2')
    col_4_3 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка4 №3')
    col_4_4 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка4 №4')
    col_4_5 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", verbose_name='колонка4 №5')
    col_4_6 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", null=True, verbose_name='колонка4 №6')
    col_4_7 = models.ImageField(upload_to=f"photos_portfolio/%Y/%m", null=True, verbose_name='колонка4 №7')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Портфолио"
        verbose_name_plural = "Портфолио"

    def get_absolute_url(self):
        return reverse('portfolio_post', kwargs={'portf_slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост блога')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    text = models.TextField(verbose_name='')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    status = models.BooleanField(default=True, verbose_name='Активно')

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ('created',)


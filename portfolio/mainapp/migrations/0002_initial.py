# Generated by Django 4.1.1 on 2023-03-13 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mainapp.blogmodel', verbose_name='Пост блога'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.category', verbose_name='Категория  '),
        ),
    ]

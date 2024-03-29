# Generated by Django 4.2.8 on 2024-01-14 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name of the book')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description of the book ')),
                ('price', models.PositiveBigIntegerField(default=2, verbose_name='price of the books')),
                ('released_book', models.DateField(verbose_name='Date of realeased')),
                ('pages', models.PositiveSmallIntegerField(verbose_name='Number of pages')),
                ('cover', models.ImageField(upload_to='books-images/', verbose_name='Cover of the book')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
    ]

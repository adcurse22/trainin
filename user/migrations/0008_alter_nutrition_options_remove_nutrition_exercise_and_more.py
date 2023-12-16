# Generated by Django 4.2.7 on 2023-12-16 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_категория_exercise_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nutrition',
            options={'verbose_name': 'Питание', 'verbose_name_plural': 'Питания'},
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='exercise',
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='nutritions/', verbose_name='Фото'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-08-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avoidsmoke', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='label',
            field=models.CharField(default='', max_length=50, verbose_name='برچسب'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.TextField(verbose_name='نکش'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=20, verbose_name='قبل از'),
        ),
    ]

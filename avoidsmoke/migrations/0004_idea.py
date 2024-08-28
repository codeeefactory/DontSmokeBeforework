# Generated by Django 5.0.2 on 2024-08-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avoidsmoke', '0003_comment_content_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('idea', models.TextField(verbose_name='ایده')),
            ],
            options={
                'verbose_name': 'Idea',
                'verbose_name_plural': 'Ideas',
            },
        ),
    ]

# Generated by Django 5.0 on 2023-12-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_subject', models.CharField(max_length=100, verbose_name='тема письма')),
                ('letter_body', models.CharField(max_length=500, verbose_name='тело письма')),
            ],
            options={
                'verbose_name': 'письмо',
                'verbose_name_plural': 'письма',
                'ordering': ('letter_subject',),
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='время рассылки')),
                ('periodicity', models.CharField(max_length=30, verbose_name='периодичность')),
                ('status', models.CharField(max_length=20, verbose_name='статус рассылки')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
                'ordering': ('status',),
            },
        ),
        migrations.CreateModel(
            name='NewsletterLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField(verbose_name='последняя попытка')),
                ('attempt_status', models.CharField(max_length=20, verbose_name='статус попытки')),
                ('server_response', models.CharField(blank=True, max_length=20, null=True, verbose_name='ответ сервера')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
                'ordering': ('date_and_time',),
            },
        ),
        migrations.CreateModel(
            name='ServiceClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('name', models.CharField(max_length=100, verbose_name='фио')),
                ('comment', models.CharField(max_length=250, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент сервиса',
                'verbose_name_plural': 'клиенты сервиса',
                'ordering': ('name',),
            },
        ),
    ]
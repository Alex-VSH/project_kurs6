from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class ServiceClient(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=100, verbose_name='фио')
    comment = models.CharField(max_length=250, verbose_name='комментарий')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'клиент сервиса'
        verbose_name_plural = 'клиенты сервиса'
        ordering = ('name',)


class Newsletter(models.Model):
    time = models.DateTimeField(verbose_name='время рассылки')
    periodicity = models.CharField(max_length=30, verbose_name='периодичность')
    status = models.CharField(max_length=20, verbose_name='статус рассылки')

    def __str__(self):
        return f'рассылка'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('status',)


class Message(models.Model):
    letter_subject = models.CharField(max_length=100, verbose_name='тема письма')
    letter_body = models.CharField(max_length=500, verbose_name='тело письма')

    def __str__(self):
        return f'письмо'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
        ordering = ('letter_subject',)


class NewsletterLogs(models.Model):
    date_and_time = models.DateTimeField(verbose_name='последняя попытка')
    attempt_status = models.CharField(max_length=20, verbose_name='статус попытки')
    server_response = models.CharField(max_length=20, verbose_name='ответ сервера', **NULLABLE)

    def __str__(self):
        return f'логи'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('date_and_time',)

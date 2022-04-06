from django.db import models


class LogFile(models.Model):
    file = models.FilePathField()
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'


class Log(models.Model):
    ip = models.GenericIPAddressField(protocol='IPv4', help_text='h')
    hyphen = models.CharField(max_length=1, default='-', help_text='l')
    userid = models.CharField(max_length=5, default='-', help_text='u, frank')
    time = models.DateTimeField(help_text='t')
    method = models.CharField(max_length=6, default='-', help_text='%r -> m')
    url = models.CharField(max_length=500, default='-', help_text='%r -> U')
    protocol = models.CharField(max_length=10, default='-', help_text='%r -> H')
    code = models.IntegerField(help_text='>s')
    size = models.IntegerField(help_text='b')
    referer = models.URLField(help_text='Referer')
    agent = models.CharField(max_length=600, help_text='User-agent')

    def __str__(self):
        return f'{self.ip} | {self.code}'

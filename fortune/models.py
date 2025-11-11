from django.db import models
from django.utils import timezone

class Uranai(models.Model):
    daikichi = models.IntegerField('大吉回数', blank=True, null=True, default=0)
    chukichi = models.IntegerField('中吉回数', blank=True, null=True, default=0)
    shokichi = models.IntegerField('小吉回数', blank=True, null=True, default=0)
    date = models.DateTimeField('日付', default=timezone.now)
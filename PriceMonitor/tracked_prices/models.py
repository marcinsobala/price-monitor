from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class TrackedPrice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    url = models.URLField(max_length=500)

    current = models.FloatField()
    currency = models.CharField(max_length=5)

    CHOICES = (
        ('A', 'Gdy cena spadnie'),
        ('B', 'Gdy cena spadnie o x procent'),
        ('C', 'Gdy cena osiągnie pożądaną wartość')
    )
    when_inform = models.CharField(max_length=1, choices=CHOICES, default='A')
    desired = models.FloatField(default=1)
    percent_drop = models.PositiveSmallIntegerField(default=10, validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])

    last_checked_date = models.DateTimeField(default=timezone.now)

    def track(self):
        self.last_checked_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.URLField(max_length=100)

    def __str__(self):
        return self.name[7:]



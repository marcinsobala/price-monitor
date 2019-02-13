from django.db import models
from django.conf import settings
from django.utils import timezone


class TrackedPrice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    current = models.FloatField()
    desired = models.FloatField()
    currency = models.CharField(max_length=5)
    url = models.URLField(max_length=500)
    last_checked_date = models.DateTimeField(default=timezone.now)

    def track(self):
        self.last_checked_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product_url[:50]

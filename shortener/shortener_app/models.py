from django.db import models

class Sortener(models.Model):
    long_urls = models.TextField()
    short_urls = models.TextField()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.short_urls
    
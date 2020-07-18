from django.db import models

MAX_SEARCH_LENGTH = 250
DJANGO_USERNAME_MAX_LENGTH = 150

class Search(models.Model):
    search = models.CharField(max_length=MAX_SEARCH_LENGTH)
    username = models.CharField(max_length=DJANGO_USERNAME_MAX_LENGTH, null=True)

    def __str__(self):
        return self.search
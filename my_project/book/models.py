from django.db import models

class Book(models.Model):
    name = models.CharField(max_length =50)
    author_name = models.CharField(max_length =50)
    year = models.IntegerField()

    def __str__(self):
        return self.name
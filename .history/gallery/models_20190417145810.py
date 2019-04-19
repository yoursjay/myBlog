from django.db import models

# Create your models here.


class Gallery(models.Model):
    """Model definition for Gallery."""
    description = models.CharField(max_length=100)

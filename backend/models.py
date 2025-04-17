from django.db import models

class DisabledPerson(models.Model):
    name = models.CharField(max_length=100)
    disability_type = models.CharField(max_length=100)
    contact = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

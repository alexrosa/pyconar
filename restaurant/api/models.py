from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(max_length=400, blank=False, null=False)
    reservation_date = models.DateTimeField(null=False)
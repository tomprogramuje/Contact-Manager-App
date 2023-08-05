from django.db import models

# Create your models here.


class Contact(models.Model):
    firstname = models.CharField(max_length=15, verbose_name="First name")
    lastname = models.CharField(max_length=15, verbose_name="Last name")
    phone_number = models.CharField(max_length=9)
    email = models.EmailField()

    class Meta:
        ordering = ["lastname"]

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

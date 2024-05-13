from django.db import models

class Client(models.Model):
    company_name = models.CharField(max_length=255, verbose_name="Name")
    phone = models.CharField(max_length=20, verbose_name="Phone")
    email = models.EmailField(verbose_name="E-mail")

    def __str__(self):
        return self.company_name

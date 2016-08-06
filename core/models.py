from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name + ' - ' + self.email

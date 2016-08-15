from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    code_confirm = models.CharField(max_length=100, default='')
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.email

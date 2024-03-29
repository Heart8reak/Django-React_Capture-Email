from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class EmailCapture(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    email           = models.EmailField()
    timestamp       = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
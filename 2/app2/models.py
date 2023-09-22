from django.db import models

# Create your models here.
class NSModel(models.Model):
    title2 = models.CharField(max_length=40,default='')
    body2 = models.CharField(max_length=50,default='')
    status2 = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title2
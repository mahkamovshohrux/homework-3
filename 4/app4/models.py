from django.db import models

# Create your models here.
class Nmodel4(models.Model):
    title4 = models.CharField(max_length=40, default="")
    body4 = models.CharField(max_length=50,default='')
    status4 = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title4

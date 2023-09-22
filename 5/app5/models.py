from django.db import models

# Create your models here.
class nModels(models.Model):
    title5 = models.CharField(max_length=40, default="")
    body5 = models.CharField(max_length=50,default="")
    status5 = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title5

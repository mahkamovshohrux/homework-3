from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CusUser(AbstractUser):
    CHOICE_ROLES = (
        (3, 'admin4'),
        (2,'staff4'),
        (1,'user4')
    )
    roles = models.PositiveIntegerField(choices=CHOICE_ROLES, default=1)

    def __str__(self) -> str:
        return self.username
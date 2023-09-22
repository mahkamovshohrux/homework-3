from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CastnUser2(AbstractUser):
    CHOICE_ROLES = (
        (3,'admin2'),
        (2,'staff2'),
        (1,'user2')
    )
    roles = models.PositiveIntegerField(choices=CHOICE_ROLES,default=1)

    def __str__(self) -> str:
        return self.username
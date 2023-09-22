from rest_framework.serializers import ModelSerializer
from .models import Nmodel4

class NSerializer4(ModelSerializer):
    class Meta:
        model = Nmodel4
        fields = ("__all__")
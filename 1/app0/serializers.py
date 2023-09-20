from rest_framework.serializers import ModelSerializer
from .models import Nmodel

class NSerializer(ModelSerializer):
    class Meta:
        model = Nmodel
        fields = ("__all__")
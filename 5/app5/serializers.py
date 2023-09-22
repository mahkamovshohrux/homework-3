from rest_framework import serializers
from .models import nModels

class nSerializers(serializers.ModelSerializer):
    class Meta:
        model =nModels
        fields = ('__all__')
from rest_framework import serializers
from .models import NSModel

class NSSerializers(serializers.ModelSerializer):
    class Meta:
        model = NSModel
        fields = ('__all__')
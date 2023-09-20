from .models import Nmodel2
from rest_framework.serializers import ModelSerializer


class Nserializers2(ModelSerializer):
    model = Nmodel2
    fields = ('__all__')
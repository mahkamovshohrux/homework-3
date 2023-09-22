from django.shortcuts import render
from rest_framework import generics
from .models import nModels
from .serializers import nSerializers
from rest_framework.permissions import IsAuthenticated
from .permission import Adminpermissionclass,Staffpermissionclass

# Create your views here.


class ListAPiView5(generics.ListAPIView):
    queryset = nModels.objects.all()
    serializer_class = nSerializers
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return nModels.objects.filter(status4=True)
class CreateAPiView5(generics.CreateAPIView):
    queryset = nModels.objects.all()
    serializer_class = nSerializers
    permission_classes = (IsAuthenticated,Staffpermissionclass)

class UpdateStatus5(generics.RetrieveUpdateDestroyAPIView):
    queryset = nModels.objects.all()
    serializer_class = nSerializers
    permission_classes = (IsAuthenticated,Adminpermissionclass)

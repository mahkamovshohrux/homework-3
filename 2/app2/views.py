from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import NSModel
from .serializers import NSSerializers
from .permission import Adminpermission,Staffpermissin


# Create your views here.
class ListAll(generics.ListAPIView):
    queryset = NSModel.objects.all()
    serializer_class = NSSerializers
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return NSModel.objects.filter(status2=True)

class CreateAll(generics.CreateAPIView):
    queryset = NSModel.objects.all()
    serializer_class = NSSerializers
    permission_classes = (IsAuthenticated,Staffpermissin)

class UpdateAll(generics.RetrieveUpdateDestroyAPIView):
    queryset = NSModel.objects.all()
    serializer_class = NSSerializers
    permission_classes = (IsAuthenticated,Adminpermission)
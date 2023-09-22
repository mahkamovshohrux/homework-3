from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import NSerializer4
from .models import Nmodel4
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .permessions import (Staffpermissionclass,Adminpermissionclass)




class ListAPiView4(generics.ListAPIView):
    queryset = Nmodel4.objects.all()
    serializer_class = NSerializer4
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Nmodel4.objects.filter(status4=True)
class CreateAPiView4(generics.CreateAPIView):
    queryset = Nmodel4.objects.all()
    serializer_class = NSerializer4
    permission_classes = (IsAuthenticated,Staffpermissionclass)

class UpdateStatus4(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nmodel4.objects.all()
    serializer_class = NSerializer4
    permission_classes = (IsAuthenticated,Adminpermissionclass)

# Create your views here.
# class CreateAPiView4(APIView):
#     def post(self, request):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 2:
#                 serializer = NSerializer4(data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#             else:
#                 return Response({'msg':'only staff members can add'})
#         else:
#             return Response({'msg':'only staff members can add'})
# class ListAPiView4(APIView):
#     def get(self, request,*args,**kwargs):
#         if str(request.user) == 'AnonymousUser':
#             return Response({'msg': 'Pleas log in'})
#         all = Nmodel4.objects.filter(status4=False)
#         serializers = NSerializer4(all,many=True)
#         return Response(serializers.data)
# class UpdateStatus4(APIView):
#     def patch(self,request,*args,**kwargs):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 3:
#                 news = get_object_or_404(Nmodel4,id=kwargs['n_id4'])
#                 serializers = NSerializer4(news,data=request.data, partial=True)
#                 if serializers.is_valid():
#                     serializers.save()
#                     return Response(serializers.data)
#                 return Response(serializers.errors)
#             else:
#                 return Response({'msg':'only admin members can add'})
#         else:
#             return Response({'msg':'only admin members can add'})
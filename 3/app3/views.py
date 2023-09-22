from django.shortcuts import get_object_or_404
from .serializers import Nserializers2
from .models import Nmodel2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permission import (StaffPermission3,AdminPrmission3)

# Create your views here.

class CreateApiew2(generics.CreateAPIView):
    queryset = Nmodel2.objects.all()
    serializer_class = Nserializers2
    permission_classes = (IsAuthenticated, StaffPermission3)


# class CreateApiew3(APIView):
#     def post(self,request):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 2:
#                 serializers = Nserializers3(data=request.data)
#                 if serializers.is_valid():
#                     serializers.save()
#                     return Response(serializers.data)
#                 return Response(serializers.errors)
#             else:
#                 return Response({'only staff2 members can add'})
#         else:
#             return Response({'only staff2 members can add'})
        
class ListApiView2(generics.ListAPIView):
    queryset = Nmodel2.objects.all()
    serializer_class = Nserializers2
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Nmodel2.objects.filter(status2=True)

# class ListApiView3(APIView):
#     def get(self, request,):
#         if str(request.user) == 'AnonymousUser':
#             return Response({'pleas log in'})
#         all3 = Nmodel3.objects.filter(status=True)
#         serializers = Nserializers3(all3,many=True)
#         return Response(serializers.data)

class UpdateStatus2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nmodel2.objects.all()
    serializer_class = Nserializers2
    permission_classes = (IsAuthenticated,AdminPrmission3)
    

# class UpdateStatus3(APIView):
#     def patch(self,request,*args,**kwargs):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 3:
#                 news3 =get_object_or_404(Nmodel3,id=kwargs['n1_id'])
#                 serializers = Nserializers3(news3,data=request.data,partial=True)
#                 if serializers.is_valid():
#                     serializers.save()
#                     return Response(serializers.data)
#                 return Response(serializers.errors)
#             else:
#                 return Response({'only admin members can add'})
#         else:
#             return Response({'only admin members can add'})
            


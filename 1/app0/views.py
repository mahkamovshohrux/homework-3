from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import NSerializer
from .models import Nmodel
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import AdminPermission,StaffPermission
from rest_framework import generics



# Create your views here.

class CreateAPiView1(generics.CreateAPIView):
    queryset = Nmodel.objects.all()
    serializer_class = NSerializer
    permission_classes = (IsAuthenticated,StaffPermission)

class ListAPiView(generics.ListAPIView):
    queryset = Nmodel.objects.all()
    serializer_class = NSerializer
    permission_classes = (IsAuthenticated,)

class UpdateStatus(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nmodel.objects.all()
    serializer_class = NSerializer
    permission_classes = (IsAuthenticated,AdminPermission)

# class CreateAPiView(APIView):
#     def post(self, request):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 2:
#                 serializer = NSerializer(data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#             else:
#                 return Response({'msg':'only staff members can add'})
#         else:
#             return Response({'msg':'only staff members can add'})
# class ListAPiView(APIView):
#     def get(self, request,*args,**kwargs):
#         if str(request.user) == 'AnonymousUser':
#             return Response({'msg': 'Pleas log in'})
#         all = Nmodel.objects.filter(status=True)
#         serializers = NSerializer(all,many=True)
#         return Response(serializers.data)
# class UpdateStatus(APIView):
#     def patch(self,request,*args,**kwargs):
#         if str(request.user) != 'AnonymousUser':
#             if request.user.roles == 3:
#                 news = get_object_or_404(Nmodel,id=kwargs['n_id'])
#                 serializers = NSerializer(news,data=request.data, partial=True)
#                 if serializers.is_valid():
#                     serializers.save()
#                     return Response(serializers.data)
#                 return Response(serializers.errors)
#             else:
#                 return Response({'msg':'only admin members can add'})
#         else:
#             return Response({'msg':'only admin members can add'})
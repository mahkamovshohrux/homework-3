from django.shortcuts import get_object_or_404
from .serializers import Nserializers2
from .models import Nmodel2
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CreateApiew2(APIView):
    def post(self,request):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 2:
                serializers = Nserializers2(data=request.data)
                if serializers.is_valid():
                    serializers.save()
                    return Response(serializers.data)
                return Response(serializers.errors)
            else:
                return Response({'only staff2 members can add'})
        else:
            return Response({'only staff2 members can add'})

class ListApiView2(APIView):
    def get(self, request,):
        if str(request.user) == 'AnonymousUser':
            return Response({'pleas log in'})
        all2 = Nmodel2.objects.filter(status=True)
        serializers = Nserializers2(all2,many=True)
        return Response(serializers.data)

class UpdateStatus2(APIView):
    def patch(self,request,*args,**kwargs):
        if str(request.user) != 'AnonymousUser':
            if request.user.roles == 3:
                news =get_object_or_404(Nmodel2,id=kwargs['n1_id'])
                serializers = Nserializers2(news,data=request.data,partial=True)
                if serializers.is_valid():
                    serializers.save()
                    return Response(serializers.data)
                return Response(serializers.errors)
            else:
                return Response({'only admin members can add'})
        else:
            return Response({'only admin members can add'})
            


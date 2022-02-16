from multiprocessing import context
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
        Classroom,
    )
from .serializer import (
        ClassRoomSerializer,
    )

class ClassRoomListView(APIView):
    def get(self,request):
        qset = Classroom.objects.all()
        ser = ClassRoomSerializer(qset,many=True)#,context={'request':request})
        return Response(ser.data)
        
    # def 


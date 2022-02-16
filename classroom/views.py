from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status as S


from .models import (
        Classroom,
        Teacher,
    )
from .serializer import (
        ClassRoomSerializer,
        TeacherSerializer,
    )

class ClassRoomListView(APIView):
    def get(self,request):
        qset = Classroom.objects.all()
        ser = ClassRoomSerializer(qset,many=True)#,context={'request':request})
        return Response(ser.data)
        
    # def 

class  TeacherViewList(APIView):
    def get(self,request):
        qset = Teacher.objects.all()
        sz = TeacherSerializer(qset,many=True,context={"request":request})
        return Response(sz.data)

    def post(self,req:Request):
        sz = TeacherSerializer(data=req.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(sz.data,status=S.HTTP_201_CREATED)
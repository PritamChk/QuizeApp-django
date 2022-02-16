from rest_framework.generics import ListCreateAPIView
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
from classroom import serializer

class ClassRoomListView(ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassRoomSerializer
   

class TeacherViewList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
        
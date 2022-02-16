from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status as S
from django.db.models import F

from classroom.serializers.quiz_set_sz import QuestionSerializer


from .models import (
        Classroom,
        Question,
        QuizSet,
        Teacher,
    )
from .serializer import (
        ClassRoomSerializer,
        TeacherSerializer,
        QuizSetSerializer,
    )
from classroom import serializer

class ClassRoomListView(ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassRoomSerializer
   

class TeacherViewList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class QuestionSetViewList(ListCreateAPIView):
    queryset = Question.objects.select_related('quizset').prefetch_related('options').all()
    serializer_class = QuestionSerializer
    
            
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from django.db.models import F



from .models import (
        Classroom,
        Question,
        QuizSet,
        Student,
        Teacher,
    )
from .serializer import (
        ClassRoomSerializer,
        TeacherSerializer,
        QuizSetSerializer,
        QuestionSerializer,
    )

def show_students(request):
    qset = Student.objects.all()
    return render(request,'index.html',{"students":list(qset)})
    

class ClassRoomListView(ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassRoomSerializer
   

class TeacherViewList(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class QuestionSetViewList(ListCreateAPIView):
    queryset = Question.objects.select_related('quizset').prefetch_related('options').all()
    serializer_class = QuestionSerializer

class QuizSetSetViewList(ListCreateAPIView):
    queryset = QuizSet.objects.prefetch_related('qustions').all()
    serializer_class = QuizSetSerializer
    
            
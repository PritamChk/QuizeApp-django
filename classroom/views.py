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

# def show_students(request):
#     qset = Student.objects.all()
#     return render(request,'index.html',{"students":list(qset)})
    

class ClassRoomView(ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassRoomSerializer
   

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.prefetch_related('quizsets').all()
    serializer_class = TeacherSerializer

class QuestionSetView(ModelViewSet):
    queryset = Question.objects.select_related('quizset').prefetch_related('options').all()
    serializer_class = QuestionSerializer

class QuizSetView(ModelViewSet):
    queryset = QuizSet.objects.all()
    serializer_class = QuizSetSerializer
    
            
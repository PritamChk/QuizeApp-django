from rest_framework.generics import ListCreateAPIView
from django.db.models import F



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
        QuestionSerializer,
    )

class ClassRoomListView(ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassRoomSerializer
   

class TeacherViewList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class QuestionSetViewList(ListCreateAPIView):
    queryset = Question.objects.select_related('quizset').prefetch_related('options').all()
    serializer_class = QuestionSerializer

class QuizSetSetViewList(ListCreateAPIView):
    queryset = QuizSet.objects.all()
    serializer_class = QuizSetSerializer
    
            
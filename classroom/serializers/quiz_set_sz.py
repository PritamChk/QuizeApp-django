from rest_framework.serializers import (
    ModelSerializer as ms ,
    SerializerMethodField as method_field,
    PrimaryKeyRelatedField as pkf,
    )

from ..models import Option, Question, QuizEvent, QuizSet
from .teacher_sz import TeacherSerializer


class OptionSerializer(ms):
    """
        # Serializes Option Model 
    """
    class Meta:
        model = Option
        fields = [ 
            "id",
            "option_value",
            "is_correct",
        ]
        read_only_fields = ["id"]
        # write_only_fields = ["is_correct"]
    
class QuestionSerializer(ms):
    """
        # Serializes Question Model
        
        >    - with options
    """
    options = OptionSerializer(Option,many = True)
    class Meta:
        model = Question
        fields = [ 
            "id",
            "question_value",
            "point",
            "options",
            "quizset",
        ]
        read_only_fields = ["id"]
        # depth = 1
    
class QuizSetSerializer(ms):
    # questions= QuestionSerializer(Question)
    class Meta:
        model = QuizSet
        fields = [
            "id",
            "heading",
            "difficulty_level",
            "author_teacher",
            "questions"
        ]    
        read_only_fields = ["id"]
        # author_teacher = TeacherSerializer(many=True)
        # depth = 1
        extra_kwargs = {
                "password":{
                    "write_only":True
                    }
                }
    # def get_questions(self,obj:QuizSet):
    #     return QuizSet.objects.prefetch_related('qustions').all()
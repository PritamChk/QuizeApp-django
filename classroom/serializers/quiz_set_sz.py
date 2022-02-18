from rest_framework.serializers import (
    ModelSerializer as ms ,
    SerializerMethodField as method_field,
    PrimaryKeyRelatedField as pkf,
    HyperlinkedRelatedField as href
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
    quizset = href(view_name='quizset-detail',read_only=True)
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
    # qustions= QuestionSerializer(Question,many=True)
    qustions= href(view_name='qus-set',many=True,read_only= True)
    qustions= href(
        many = True,
        read_only = True,
        view_name='qus-detail'
    )
    class Meta:
        model = QuizSet
        fields = [
            "id",
            "heading",
            "difficulty_level",
            "author_teacher",
            "qustions"
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
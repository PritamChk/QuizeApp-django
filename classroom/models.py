from datetime import date, datetime, time, timedelta, timezone
from uuid import uuid4

from django.core.validators import MaxValueValidator
from django.db.models import (
    CASCADE, PROTECT, SET_NULL, BooleanField,
    CharField, DateField, DateTimeField,
    DurationField, EmailField, ForeignKey,
    IntegerField, ManyToManyField, Model,
    OneToOneField, PositiveSmallIntegerField,
    TextField, TimeField, UUIDField
)

STR_MAX_LEN = 300


class Classroom(Model):
    title = CharField(max_length=STR_MAX_LEN)
    subject = CharField(max_length=STR_MAX_LEN)
    #teachers = ...

    def __str__(self) -> str:
        return self.title[:15] + " " + self.subject[:15]

    def count_teachers(self):
        return Teacher.objects.prefetch_related('classroom').filter(classroom__id=self.id).count()

    def count_students(self):
        return Student.objects.prefetch_related('classroom').filter(classroom__id=self.id).count()


class BaseUser(Model):
    first_name = CharField(max_length=STR_MAX_LEN)
    last_name = CharField(max_length=STR_MAX_LEN)
    email = EmailField(unique=True, db_index=True)
    username = CharField(max_length=60, unique=True, db_index=True)
    password = CharField(max_length=STR_MAX_LEN)
    joined_at = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ["first_name", "last_name", "-joined_at"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(BaseUser):
    classroom = ManyToManyField(
        "Classroom", related_name="teachers", blank=True)

    class Meta(BaseUser.Meta):
        pass

    def count_classroom(self):
        count_class = self.classroom.count()
        return count_class


class Student(BaseUser):
    classroom = ManyToManyField(Classroom, related_name="students", blank=True)

    class Meta(BaseUser.Meta):
        pass

    def count_classroom(self):
        count_class = self.classroom.count()
        return count_class


class Question(Model):
    question_value = TextField()
    point = PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(
        15, "Hya hya, 1ta mcq tei 100 marks diye dao,Ajob Public")])
    updated_at = DateTimeField(auto_now=True)
    quizset = ForeignKey("QuizSet", on_delete=CASCADE, related_name="qustions")
    #options = ...

    class Meta:
        ordering = ["point"]

    def __str__(self) -> str:
        return self.question_value.lower()[:20]


class Option(Model):
    option_value = CharField(
        max_length=500, default="None Of The Above", blank=True)
    is_correct = BooleanField(default=False, editable=True)
    qustion = ForeignKey(Question, on_delete=CASCADE, related_name="options")
    # belongs_to_quiz_set = ForeignKey("QuizSet",on_delete=CASCADE,related_name="qus_options")

    def __str__(self) -> str:
        return self.option_value.lower()[:15]


class QuizEvent(Model):
    title = CharField(max_length=STR_MAX_LEN, default=uuid4,
                      blank=True, db_index=True)
    start_date = DateField(default=date.today() +
                           timedelta(days=1), blank=True, db_index=True)
    start_time = TimeField(default=datetime.now().time(),
                           blank=True, db_index=True)
    exam_duration = DurationField(default=timedelta(hours=1), blank=True)
    all_qsets = ManyToManyField(
        "QuizSet", related_name="quiz_event_part", blank=True)
    host_classroom = ForeignKey(
        Classroom, on_delete=CASCADE, related_name="hosted_quizes")
    # quizsets

    class Meta:
        ordering = [
            "start_date",
            "start_time",
            "-exam_duration",
            "title"
        ]

    def __str__(self) -> str:
        return self.title[:7]+"..."


class QuizSet(Model):
    LEVEL_EASY = "E"
    LEVEL_MEDIUM = "M"
    LEVEL_HARD = "H"
    LEVEL = [
        (LEVEL_EASY, "Easy"),
        (LEVEL_MEDIUM, "Medium"),
        (LEVEL_HARD, "Hard"),
    ]

    heading = CharField(max_length=STR_MAX_LEN,
                        default=uuid4, db_index=True, blank=True)
    created_at = DateTimeField(auto_now_add=True, db_index=True)
    update_at = DateTimeField(auto_now=True, editable=False)
    difficulty_level = CharField(
        max_length=2, choices=LEVEL, default=LEVEL_EASY)
    author_teacher = ForeignKey(
        Teacher, on_delete=CASCADE, related_name='quizsets')
    quiz_event = ForeignKey(QuizEvent, on_delete=SET_NULL,
                            null=True, blank=True, related_name="quizsets")
    #questions = ...

    class Meta:
        ordering = ["-created_at", "difficulty_level"]

    def __str__(self) -> str:
        return f"{self.heading[:10]}"


class AnswerSet(Model):
    id = UUIDField(primary_key=True,default=uuid4,editable=False)
    quizevent = ForeignKey(QuizEvent,on_delete=PROTECT,related_name="answer_sets")
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)
    # answers = ...
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return str(self.id)
    
class Answer(Model):
    qid = IntegerField()
    qzid = IntegerField()
    optid = IntegerField() 
    created_at = DateField(auto_now_add=True)
    updated_at = DateField(auto_now=True)
    student = ForeignKey(Student,on_delete=CASCADE,related_name='answers')
    answer_set = ForeignKey(AnswerSet,on_delete=PROTECT,related_name='answers') 
    
    # class Meta:
    #     ordering = [ 
    #         "created_at",
    #         "quizset_id",
    #         "qus_id"
    #     ]

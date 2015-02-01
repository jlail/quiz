from django.db import models


class Question(models.Model):
    answer_object = models.ForeignKey('Answer')
    question_text = models.TextField()
    question_category = models.CharField(max_length=200)
    previous_attempt_correct = models.BooleanField(default=False)
    number_of_answers = models.IntegerField()


class Answer(models.Model):
    question_object = models.ForeignKey('Question')
    answer_text = models.TextField()
    answer_category = models.CharField(max_length=200)
    number_of_answers = models.IntegerField()
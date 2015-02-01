from django.contrib import admin
from quizapp.models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('question_text', 'question_category')
    list_filter = ['question_category', 'number_of_answers']
    search_fields = ['question_text', 'question_category']


admin.site.register(Question, QuestionAdmin)

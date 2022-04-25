from dataclasses import fields
from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'date_created')
    search_fields = ('title', 'category__name')
    
class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    extra = 1
    
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('quiz', 'title')
    list_display = ('title', 'quiz', 'date_created')
    search_fields = ('title', 'quiz__title')
    inlines = [AnswerInlineModel]
    
@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'is_right')
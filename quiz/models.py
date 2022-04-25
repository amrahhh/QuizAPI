from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Category(models.Model):
    #information's
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['id']
    
    def __str__(self):
        return self.name


class Quiz(models.Model):
    #relation's
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    #information's
    title = models.CharField(max_length=100, default=_('New Quiz'), verbose_name = _('Quiz Title'))
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ['id']
        
        
class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True, verbose_name = _('Last Updated'))
    
    class Meta:
        abstract = True


class Question(Updated):
    #relation's
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING, related_name='question')
    
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert')),
    )
    
    TYPE = (
        (0, _('Multiple Choice')),
    )
    #information's
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name = _('Type of Question'))
    title = models.CharField(max_length=100, verbose_name = _('Title'))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name = _('Difficulty'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name = _('Date Created'))
    is_active = models.BooleanField(default=False, verbose_name = _('Active Status'))
        
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    def __str__(self):
        return self.title
    
    
class Answer(Updated):
    #relation's
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='answer')
    #information's
    answer_text = models.CharField(max_length=100, verbose_name = _('Answer Text'))
    is_right = models.BooleanField(default=False, verbose_name = _('Right Answer'))
    
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural =_('Answers')
        ordering = ['id']
        
    def __str__(self):
        return self.answer_text
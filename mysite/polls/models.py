from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

class Choice(models.Model):
    # REMEMBER: foreign key is an attribute that relates to another entitiy in a database
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    

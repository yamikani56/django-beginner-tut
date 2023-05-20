from django.db import models

# Create your models here.

class Question(models.Model):
    question_text= models.CharField(max_length=200) 
    pub_date=models.DateTimeField("date published")

class Choice(models.Model):
    choice_text=models.CharField(max_length=70)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    votes=models.IntegerField(default=0)
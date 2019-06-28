import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    # each field is represented by an instance of a field class
    question_text = models.CharField(max_length=200)  # max length required arg
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # set default amount of votes to 0

    def __str__(self):
        return self.choice_text

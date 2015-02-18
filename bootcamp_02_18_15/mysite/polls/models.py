from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
    	return '%s: %s' % (self.question.question_text, self.choice_text)

class Vote(models.Model):
	choice = models.ForeignKey(Choice)
	time = models.DateTimeField(auto_now_add=True)

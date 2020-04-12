from django.db import models
from django.contrib.auth.models import User


class CreatePoll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def total(self):
        return self.option_one_count + self.option_two_count

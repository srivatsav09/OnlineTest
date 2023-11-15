from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    # Add custom fields as needed
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    Class = models.IntegerField()


class Exam(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration_minutes = models.PositiveIntegerField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()


class Choice(models.Model):
    question = models.ForeignKey(
        'Question', related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)


class UserResponse(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    selected_choice = models.ForeignKey('Choice', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s response to '{self.question}'"

from django.db import models

# Create your models here.
class MbtiQuestion(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    answer = models.CharField(max_length=100)

class Mbti(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
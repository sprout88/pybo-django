from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200) # 글자수 제한 Text
    content = models.TextField() # 글자수 제한 불가
    crate_date = models.DateTimeField()

class Answer(models.Model):
    # CASCADE: ForeignKey로 연결된 Question이 삭제되면 이 Answer을 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

# Create your models here.

from django.db import models

class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=20)
    fee=models.IntegerField()
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.sname



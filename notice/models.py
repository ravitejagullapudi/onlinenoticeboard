from django.db import models

# Create your models here.
class Notice(models.Model):
    notice=models.CharField(max_length=1000)
    postedUser=models.CharField(max_length=50)
    date=models.DateField()
    Year=models.IntegerField()
    sec=models.CharField(max_length=1)
    branch=models.CharField(max_length=4)
    def __str__(self):
        return self.notice


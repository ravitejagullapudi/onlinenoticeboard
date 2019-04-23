from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.EmailField()
    enquiry=models.CharField(max_length=1000)
class Faq(models.Model):
    email=models.EmailField()
    question= models.CharField(max_length=1000)
    answer=models.CharField(max_length=1000,default='Not Answered')

    def __str__(self):
        return self.question
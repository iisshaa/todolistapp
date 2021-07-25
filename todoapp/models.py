from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    content = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.content}'

    class Meta:
        ordering = ['-date']

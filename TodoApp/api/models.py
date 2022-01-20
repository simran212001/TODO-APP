from django.db import models

# Create your models here.
# Creating a model in the database for the ToDo application that the Django ORM will manage.
class Task(models.Model):
    task_title = models.CharField(max_length=30)
    task_desc = models.TextField()
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_title
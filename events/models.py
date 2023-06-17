from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_description = models.TextField()
    slug = models.CharField(max_length=50)
    time_of_creation = models.DateTimeField('date_published',auto_now_add=True)
    event_createdby=models.CharField(max_length=50,default='')
    participants = models.ManyToManyField('Participant', related_name='registered_events')

    def __str__(self):
        return self.event_name

class Participant(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
    


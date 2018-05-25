from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns


class Topic(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the topic')
    tag = models.ManyToManyField('Tag', help_text='Add tags for this topic')
    lesson = models.ForeignKey('Lesson', on_delete=models.SET_NULL, null=True, help_text='Add lessons for this topic')
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('topics-detail', args=[str(self.id)])
    
#    def createTag(self, Tag):
        #Is this necessary? Research for tomorrow
      
    
class Tag(models.Model):
    name = models.CharField(max_length=30)
    summary = models.TextField(max_length=300, help_text='Enter a brief description of the topic')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tags-detail', args=[str(self.id)])
    
                       

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the topic')
    tag = models.ManyToManyField(Tag, help_text='Add tags for this topic')    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lessons-detail', args=[str(self.id)])
    
    
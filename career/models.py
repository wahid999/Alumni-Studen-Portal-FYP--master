from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
from djrichtextfield.models import RichTextField
POST_TYPE_CHOICES=[('Internship','Internship'),('Job','Job')]


class CareerPost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    postType=models.CharField(max_length=30,choices=POST_TYPE_CHOICES)
    description=models.TextField()
    image=models.ImageField(null=True,upload_to='Career(jobs-intership)')
    datePosted = models.DateField(auto_now_add=True)
    
  
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(CareerPost, on_delete=models.CASCADE,related_name='post')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.content

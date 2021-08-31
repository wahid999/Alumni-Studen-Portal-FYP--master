from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


class DissForum(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    datePosted = models.DateField(auto_now_add=True, editable=True)
    class Meta:
        ordering = ['datePosted']
  
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(DissForum, on_delete=models.CASCADE,related_name='post')
    user = models.ForeignKey(User, related_name='disFourmuser', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, editable=True)

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return self.content

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='author', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='profile/')



class Message(models.Model):
    contact = models.ForeignKey(Contact, related_name='author', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username


class Chat(models.Model):
    memebers_name=models.TextField(null=True)
    participants = models.ManyToManyField(Contact, related_name='chats')
    messages = models.ManyToManyField(Message, blank=True,related_name='messages')

    def __str__(self):
        return "{}".format(self.pk)
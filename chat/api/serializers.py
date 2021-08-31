from rest_framework import serializers

from chat.models import Chat, Contact
from profileDashboard.models import *
from chat.views import get_user_contact
from django.contrib.auth import get_user_model
User = get_user_model()

class ContactSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

class MessageSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '_all_'

class ProfileSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta: 
        model = Profile
        fields = ( 'user','photo_url')

    def get_photo_url(self, profile):
        request = self.context.get('request')
        photo_url = profile.profilePic.url
        return request.build_absolute_uri(photo_url)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')

class ChatSerializer(serializers.ModelSerializer):
    
    participants = ContactSerializer(many=True)
    # messages = MessageSerializer(many=True)
    class Meta:
        model = Chat
        fields = ('id', 'messages', 'participants', 'memebers_name')
        
        # fields = ('id', 'messages', 'participants','memebers_name','messages')
        # read_only = ('id')

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        chat = Chat()
        chat.save()
        curr_user = self.context['request'].user
        if (len(Contact.objects.filter(user=curr_user)) == 0):
            Contact.objects.create(user=curr_user)
        usernames=''   
        for username in participants:
            contact = get_user_contact(username)
            chat.participants.add(contact)
            usernames += username.capitalize() + '_'
        usernames=usernames[:-1]
        chat.memebers_name=usernames
        chat.save()
        return chat




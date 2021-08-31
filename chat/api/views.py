from django.contrib.auth import get_user_model
from rest_framework import permissions
from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from chat.models import Chat, Contact,Profile
from chat.views import get_user_contact
from .serializers import ChatSerializer,ProfileSerializer,UserSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import APIView

User = get_user_model()


class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset


class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )





class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ProfileDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    
    def retrieve(self, request, pk):
        try:
         user = User.objects.get(username=pk)
        except:
         return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(username=pk)
        ser = ProfileSerializer(Profile.objects.filter(user=user), context={"request": request}, many=True)
        return Response(ser.data)




class DeleteChatView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    
    def destroy(self, request, pk):
        try:
             chat = Chat.objects.get(pk=pk)
        except:
            print('okkk')
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = Contact.objects.get(user=request.user)
        username=request.user.username
        chat = Chat.objects.get(pk=pk)
    
        if len(chat.participants.all()) == 1:
            chat.delete()
        else:
            chat.participants.remove(user)
            username = username.capitalize()            
        return Response(status=status.HTTP_200_OK)


        
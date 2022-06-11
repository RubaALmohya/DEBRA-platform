from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import RegisterSerializer ,UserSettingSerializers
from .models import UserSettingModel
from datetime import date, datetime



@api_view(['GET'])
def UserRegister(request:Request):
    MembersSerializer = RegisterSerializer(data=request.data)
    if MembersSerializer.is_valid():
        NewMembers = User.objects.create_user(**MembersSerializer.data)
        NewMembers.save()
        msg = {"message":"created user successfuly"}
        return Response(msg)
    else:
        print(MembersSerializer.errors)
        msg = {"message": "Couldn't create member"}
        return Response(msg)

@api_view(['POST'])
def UserLogin(request:Request):
    if 'username' in request.data and 'password' in request.data:
        Member = authenticate(request, username = request.data['username'], password=request.data['password'])
        if Member is not None:
            token = AccessToken.for_user(Member)
            MemberData = {"message":"your token is ready  :) " ,"token" : str(token)}
            return Response(MemberData)
    return Response({"msg" : "please provide your username and password"}, status=status.HTTP_401_UNAUTHORIZED)

from datetime import date


@api_view(['POST'])
def UserSetting(request:Request):
   add_user_sitting1 = UserSettingSerializers(data=request.data)
   if add_user_sitting1.is_valid():
       add_user_sitting1.save()
       usersitting = {
           "message": "Created setting Successfully" ,
           "user setting": add_user_sitting1.data
       }
       return Response(usersitting)
   else:
       print(add_user_sitting1.errors)
       usersitting = {"msg" : "couldn't create a city"}
       return Response(usersitting ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listAllUsers(request : Request):

    users = UserSettingModel.objects.all()
    userslist = {"msg": "List of All users",
                 "users": UserSettingSerializers(instance=users, many=True).data}
    return Response(userslist)

@api_view(['GET'])
def listExperts(request : Request):
    experts = UserSettingModel.objects.filter(account_type=2)
    expertslist = {"msg": "List of experts",
                 "experts": UserSettingSerializers(instance=experts, many=True).data}
    return Response(expertslist)
@api_view(['GET'])
def listUsers(request : Request):
    users = UserSettingModel.objects.filter(account_type=1)
    userslist = {"msg": "List of  users",
                 "users": UserSettingSerializers(instance=users, many=True).data}
    return Response(userslist)



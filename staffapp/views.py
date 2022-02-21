# import self
# from django.contrib.auth.models import User
# from django.db import IntegrityError
# from django.shortcuts import render

#Create your views here.
# from rest_framework import viewsets, generics
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.exceptions import ValidationError
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import generics, permissions
# from rest_framework.response import Response


# from rest_framework import permissions
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from staffapp.models import Users
# from staffapp.serializers import UserSerializer, RegistrationSerializer, RegisterSerializer
from django.http import HttpResponse
from rest_framework.utils import json

from .models import User, Religion, Caste, Institutes, Post, Nationality
from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer, UserCreateSerializer, \
    UserLoginSerializer, ReligionSerializer, CasteSerializer, InstituteSerializer, PostSerializer, NationalitySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, viewsets

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken



class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()



class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        # if not serializer.is_valid():
        #     raise ValidationError(serializer.errors)
        if serializer.is_valid(raise_exception=True):
            new_data = {"id": serializer.data['id'], "email":serializer.data['email']}
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer

class ReligionViewSet(viewsets.ModelViewSet):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer


class CasteViewSet(viewsets.ModelViewSet):
    queryset = Caste.objects.all()
    serializer_class = CasteSerializer

    def list(self, request, *args, **kwargs):
        print(request.GET.get('religion'))
        caste = Caste.objects.filter(religion=request.GET.get('religion_id'))
        c_list = []
        for item in caste:
            c_list.append(item.caste)
        print(c_list)
        # return HttpResponse(json.dumps(c_list), status=status.HTTP_200_OK)
        return HttpResponse(json.dumps({"caste": c_list}), status=status.HTTP_200_OK)

class InstitutesViewSet(viewsets.ModelViewSet):
    queryset = Institutes.objects.all()
    serializer_class = InstituteSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        print(request.GET.get('institute_id'))
        postName = Post.objects.filter(institute=request.GET.get('institute_id'))
        p_list = []
        for item in postName:
            p_list.append(item.postName)
        print(p_list)

        return HttpResponse(json.dumps({"post": p_list}), status=status.HTTP_200_OK)



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

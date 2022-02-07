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


from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

# def registration_view(request):
#
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
# from staffapp.serializers import RegistrationSerializer

# api_view(["POST"])
# @permission_classes([AllowAny])
# def Register_Users(request):
#     try:
#         data = []
#         serializer = RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             account = serializer.save()
#             account.is_active = True
#             # password = self.validated_data["password"]
#             # account.set_password(password)
#             account.save()
#
#             token = Token.objects.get_or_create(user=account)[0].key
#             data["message"] = "user registered successfully"
#             data["email"] = account.email
#             data["username"] = account.username
#             data["token"] = token
#
#         else:
#             data = serializer.errors
#
#
#         return Response(data)
#     except IntegrityError as e:
#         account=Users.objects.get(username='')
#         account.delete()
#         raise ValidationError({"400": f'{str(e)}'})
#
#     except KeyError as e:
#         print(e)
#         raise ValidationError({"400": f'Field {str(e)} missing'})



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

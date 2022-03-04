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
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import json

from .models import User, Religion, Caste, Institutes, Post, Nationality
from .serializers import RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer, UserCreateSerializer, \
    UserLoginSerializer, ReligionSerializer, CasteSerializer, InstituteSerializer, PostSerializer, \
    NationalitySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, viewsets

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()



class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(request.data)
        serializer = UserLoginSerializer(data=data)
        # if not serializer.is_valid():
        #     raise ValidationError(serializer.errors)
        if serializer.is_valid(raise_exception=True):
            new_data = {"id": serializer.data['id'], "email": serializer.data['email']}
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(('POST', 'PUT'))
@action(detail=False, methods=['put', 'post'])
def applicant_info(request):
    reply = {}
    if request.method != "POST":
        reply['status'] = "FAILED"
        reply['message'] = "FAILED"
        dict_obj = json.dumps(reply)

        return HttpResponse(dict_obj, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        institute1 = request.POST.get('institute')
        post1 = request.POST.get('post')
        sslcInstitution1 = request.POST.get('sslcInstitution')
        sslc_year_of_study1 = request.POST.get('sslc_year_of_study')
        sslcpercentage1 = request.POST.get('sslcpercentage')

        plustwoInstitution1 = request.POST.get('plustwoInstitution')
        plustwo_year_of_study1 = request.POST.get('plustwo_year_of_study')
        plustwopercentage1 = request.POST.get('plustwopercentage')

        aadhar1 = request.POST.get('aadhar')
        nationality1 = request.POST.get('nationality')
        religion1 = request.POST.get('religion')
        caste1 = request.POST.get('caste')
        bloodGroup1 = request.POST.get('bloodGroup')
        handicapped1 = request.POST.get('handicapped')

        c_house_name1 = request.POST.get('c_house_name')
        c_city1 = request.POST.get('c_city')
        c_postoffice1 = request.POST.get('c_postoffice')
        c_district1 = request.POST.get('c_district')
        c_state1 = request.POST.get('c_state')
        c_pincode1 = request.POST.get('c_pincode')
        print(religion1,caste1, bloodGroup1,handicapped1,c_house_name1,c_city1,c_postoffice1,c_district1,c_state1, c_pincode1)
        print(institute1, post1, sslcInstitution1, sslc_year_of_study1, sslcpercentage1, plustwoInstitution1, plustwo_year_of_study1, religion1, nationality1)
        try:

            print(request.POST.get('id'))
            print(request.POST.get('institute'))
            print(request.POST.get('post'))
            customuser = User.objects.get(pk=request.POST.get('id'))
            print(customuser)
            customuser.institute = institute1

            customuser.post = post1
            customuser.sslcInstitution = sslcInstitution1
            customuser.sslc_year_of_study = sslc_year_of_study1
            customuser.sslcpercentage = sslcpercentage1
            customuser.plustwoInstitution = plustwoInstitution1
            customuser.plustwo_year_of_study = plustwo_year_of_study1
            customuser.plustwopercentage = plustwopercentage1
            customuser.aadhar = aadhar1
            customuser.nationality = nationality1
            customuser.religion = religion1
            customuser.caste = caste1
            customuser.bloodGroup = bloodGroup1
            customuser.handicapped = handicapped1
            customuser.c_house_name = c_house_name1
            customuser.c_city = c_city1
            customuser.c_postoffice = c_postoffice1
            customuser.c_district = c_district1
            customuser.c_state = c_state1
            customuser.c_pincode = c_pincode1
            customuser.save()

            print("saved")
            reply['status'] = "SUCCESS"
            reply['message'] = "Profile was successfuly added"
            dict_obj = json.dumps(reply)

            return HttpResponse(dict_obj, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('%s' % type(e))
            messages.error(request, "Failed to Update Profile")

            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


# class ApplicantInfoViewSet(viewsets.ModelViewSet):
#     queryset = ApplicantInfo.objects.all()
#     serializer_class = ApplicantInfoSerializer

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
        print(caste)
        c_list = []
        for item in caste:
            c_list.append(item.caste)
        print(c_list)
        print(json.dumps({"caste": c_list}))
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

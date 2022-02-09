# from django.contrib.auth.models import User
# from rest_framework import serializers
# from staffapp.models import Users


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = "__all__"
#     # def create(self, validated_data):
#     #     password = validated_data['password']
#     #     user = super(UserSerializer, self).create(validated_data)
#     #
#     #     user.set_password(password)
#     #     user.save()
#     #     return user
#
#
from django.contrib.auth import authenticate
from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from staffapp.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name')
        extra_kwargs = {
            'first_name': {'required': True},

        }

    def validate(self, attrs):
        print(attrs['password']);
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],

        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name',  'email')
        extra_kwargs = {
            'first_name': {'required': True},

        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.first_name = validated_data['first_name']

        instance.email = validated_data['email']
        instance.username = validated_data['email']

        instance.save()

        return instance


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # print("Inside the Create Function")
        user = User.objects.create_complete_user(validated_data['name'],
                                                 validated_data['email'],
                                                 validated_data['dob'],
                                                 validated_data['gender'],
                                                 validated_data['phoneNumber'],
                                                 validated_data['password'],
                                                 )
        return user

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'dob', 'gender', 'phoneNumber']
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs, ):
        user = authenticate(
            email=attrs['email'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('invalid credentials provided')
        self.instance = user
        return user

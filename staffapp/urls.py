from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from staffapp import views
# from staffapp.views import RegisterAPI
from staffapp.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView, \
    UserCreateAPIView, UserLoginAPIView

router = routers.DefaultRouter()

router.register(r'religion', views.ReligionViewSet)
router.register(r'caste', views.CasteViewSet)
router.register(r'nationality', views.NationalityViewSet)
router.register(r'institutes', views.InstitutesViewSet)
router.register(r'post', views.PostViewSet)
# router.register(r'user/applicantinfo', views.ApplicantInfoViewSet),


urlpatterns = [
    path('', include(router.urls)),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # To get access token

    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('user/applicantInfo/', views.applicant_info, name="get_user_details"),

    path('user/register/', UserCreateAPIView.as_view(), name='user-register'),
    path('user/login/', UserLoginAPIView.as_view(), name="user-login"),


]
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from staffapp import views
# from staffapp.views import RegisterAPI
from staffapp.views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView

router = routers.DefaultRouter()

# router.register(r'user', views.UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    # path('user/', UserViewSet, name='users' ),
    # path('register/', views.Register_Users),
    # path('api/register/', RegisterAPI.as_view(), name='register'),
]
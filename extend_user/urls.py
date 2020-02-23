from django.urls import path, include
from rest_framework.routers import DefaultRouter
from extend_user.auth import CustomAuthToken
from extend_user.views import UserViewSet, CreateUserAPIView, RoleViewSet

router = DefaultRouter()
router.register(r'auth/user', UserViewSet)
router.register(r'auth/role', RoleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'api-token-auth/', CustomAuthToken.as_view()),
    path('auth/user/create', CreateUserAPIView.as_view()),
]
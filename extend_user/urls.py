from django.urls import path, include
from rest_framework.routers import DefaultRouter
from extend_user.auth import CustomAuthToken
from extend_user.views import UserViewSet

router = DefaultRouter()
router.register(r'auth/user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'api-token-auth/', CustomAuthToken.as_view())
]
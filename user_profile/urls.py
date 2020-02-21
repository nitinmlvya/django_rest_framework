from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user_profile import views

router = DefaultRouter()
# router.register(r'auth/user', views.UserViewSet)
router.register(r'user_profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
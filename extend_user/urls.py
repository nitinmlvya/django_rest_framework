from django.urls import path, include
from rest_framework.routers import DefaultRouter
from extend_user import views

router = DefaultRouter()
router.register(r'auth/user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
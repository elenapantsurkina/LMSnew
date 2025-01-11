from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

from .views import PaymentViewSet, UserCreateAPIView, UserViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payments", PaymentViewSet)

router = SimpleRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
]

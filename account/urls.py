from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import UserView

app_name = 'accounts'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', UserView.as_view(),name='profile_view'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
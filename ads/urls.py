from django.urls import path
from .views import AdlistView

app_name = 'ads'

urlpatterns = [
    path('list/', AdlistView.as_view(), name='adlist'),
]
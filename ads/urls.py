from django.urls import path
from .views import AdlistView, AdCreateView, AdDetailView

app_name = 'ads'

urlpatterns = [
    path('list/', AdlistView.as_view(), name='ad-list'),
    path('create/', AdCreateView.as_view(), name='ad-create'),
    path('detail/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
]
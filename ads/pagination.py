from rest_framework.pagination import PageNumberPagination
from django.conf import settings

class StandardPagination(PageNumberPagination):
    page_size = getattr(settings, 'PAGINATION_PAGE_SIZE', 1)
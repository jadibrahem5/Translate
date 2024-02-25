from django.urls import path
from .views import TranslationRequestAPI

urlpatterns = [
    path('translation-request/', TranslationRequestAPI.as_view(), name='translation_request_api'),
]
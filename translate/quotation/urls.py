from django.urls import path
from .views import TranslationRequestAPI, hello_view 
urlpatterns = [
     path('', hello_view, name='hello'),
     path('translation-request/', TranslationRequestAPI.as_view(), name='translation_request_api'),
]

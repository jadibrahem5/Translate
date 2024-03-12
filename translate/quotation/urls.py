from django.urls import path
from .views import TranslationRequestAPI, hello_view 
urlpatterns = [
     path('api/hello/', hello_view, name='hello'),
     path('api/', TranslationRequestAPI.as_view(), name='translation_request_api'),
]

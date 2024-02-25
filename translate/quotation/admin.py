from django.contrib import admin
from .models import TranslationRequest  # Import your model

# Register your model with the admin site
admin.site.register(TranslationRequest)
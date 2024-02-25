from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TranslationRequestSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

class TranslationRequestAPI(APIView):
    renderer_classes = [JSONRenderer]  # Ensure responses are rendered as JSON
    parser_classes = [JSONParser]  # Ensure requests are parsed as JSON

    def post(self, request, format=None):
        serializer = TranslationRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the translation request to the database

            # Prepare the email content
            subject = f"New Translation Request from: {serializer.validated_data['requester_name']}"
            message = (f"Request from: {serializer.validated_data['requester_name']}\n"
                       f"Email: {serializer.validated_data['email']}\n"
                       f"Phone: {serializer.validated_data['phone']}\n"
                       f"Description: {serializer.validated_data['description']}")
            from_email = 'w699767@gmail.com'  # Your Gmail address
            recipient_list = ['w699767@gmail.com']  # Email recipient(s)

            # Send an email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
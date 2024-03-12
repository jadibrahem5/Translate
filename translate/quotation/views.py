from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import TranslationRequestSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class TranslationRequestAPI(APIView):
    renderer_classes = [JSONRenderer]  # Ensure responses are rendered as JSON
    parser_classes = [JSONParser]  # Ensure requests are parsed as JSON

    def get(self, request, format=None):
        # This is just a simple test method
        test_data = {
            'message': 'This is a test response from GET request.'
        }
        return Response(test_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TranslationRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the translation request to the database

            # Prepare the email content
            subject = f"New Translation Request from: {serializer.validated_data.get('requester_name', 'Anonymous')}"
            message = (f"Request from: {serializer.validated_data.get('requester_name', 'Anonymous')}\n"
                       f"Email: {serializer.validated_data.get('email', 'Not provided')}\n"
                       f"Phone: {serializer.validated_data.get('phone', 'Not provided')}\n"
                       f"Description: {serializer.validated_data.get('description', 'Not provided')}")
            from_email = 'w699767@gmail.com'  # Your Gmail address
            recipient_list = ['w699767@gmail.com']  # Email recipient(s)

            try:
                # Send an email
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            except Exception as e:
                # If sending the email fails, log the error and return a 500 Internal Server Error response
                # You might want to log the error more gracefully or send it to an error tracking service
                print(f"Error sending email: {str(e)}")
                return Response({'error': 'Internal server error, failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # If the serializer is not valid, return a 400 Bad Request response with the error details
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

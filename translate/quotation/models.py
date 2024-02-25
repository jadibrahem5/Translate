from django.db import models

class TranslationRequest(models.Model):
    requester_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester_name} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

from rest_framework import authentication, generics, permissions

from .models import EmailCapture
from .serializers import EmailCaptureCreateSerializers



class EmailCaptureCreateAPIView(generics.CreateAPIView):
    queryset                = EmailCapture.objects.all()
    serializer_class        = EmailCaptureCreateSerializers
    authentication_classes  = [authentication.SessionAuthentication]
    permission_classes      = [permissions.AllowAny]


    def perform_create(self, serializer):
        request = self.request
        user = request.user 
        if not user.is_authenticated:
            user = None 
        serializer.save(user=user)


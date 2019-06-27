from rest_framework import serializers


from.models import EmailCapture


class EmailCaptureCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailCapture
        fields = [
            'email',
        ]


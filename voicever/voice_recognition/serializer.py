from rest_framework.serializers import Serializer,FileField,ValidationError
import os
class VoiceRecogntionSerializer(Serializer):
    sample = FileField()
    def validate(self, attrs):
        allowed_extensions = ['.wav']
        _,file_extension = os.path.splitext((attrs['sample'].name).lower())
        if file_extension in allowed_extensions:
            return attrs
        else:
            raise ValidationError(
                {
                    "Error":"Inappropriate File Format"
                }
            )
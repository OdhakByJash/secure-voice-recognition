from rest_framework.serializers import Serializer,FileField,ValidationError
import os
class VoiceRecogntionSerializer(Serializer):
    sample = FileField()
    def validate(self, attrs):
        allowed_extensions = ['.mp3', '.mp4', '.mpeg', '.mpga', '.m4a', '.wav','.webm']
        _,file_extension = os.path.splitext((attrs['sample'].name).lower())
        if file_extension in allowed_extensions:
            return attrs
        else:
            raise ValidationError(
                {
                    "Error":"Inappropriate File Format"
                }
            )
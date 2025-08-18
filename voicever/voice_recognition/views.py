from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from voice_recognition.serializer import VoiceRecogntionSerializer
from voice_recognition.models import AuthenticUserVoice
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register(request):
    try:
        serializer = VoiceRecogntionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthenticUserVoice.objects.create(
            sample = serializer.validated_data['sample'],
            user = request.user
        )
        return Response(
            {
                "Status":"Voice Sample Registered"
            },status=HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                "Status":"Voice Sample Registration Failed",
                "Error":str(e)
            },status=HTTP_400_BAD_REQUEST
        )
def verify(request):
    try:
        serializer = VoiceRecogntionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response()
    except Exception as e:
        return Response()
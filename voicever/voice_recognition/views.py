from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from voice_recognition.serializer import VoiceRecogntionSerializer
from voice_recognition.models import RegistrationUserVoice,VerificationUserVoice
import torchaudio
from speechbrain.pretrained import SpeakerRecognition
from django.conf.global_settings import MEDIA_ROOT
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register(request):
    try:
        serializer = VoiceRecogntionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        RegistrationUserVoice.objects.create(
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
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify(request):
    try:
        serializer = VoiceRecogntionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        verification_instance = VerificationUserVoice.objects.create(
            sample = serializer.validated_data['sample'],
            user = request.user
        )
        registration_instance = RegistrationUserVoice.objects.get(user=request.user)
        verification = SpeakerRecognition.from_hparams(
            source="speechbrain/spkrec-ecapa-voxceleb"
        )
        signal1, fs1 = torchaudio.load(verification_instance.sample.path)
        signal2, fs2 = torchaudio.load(registration_instance.sample.path)
        score,pred = verification.verify_files(signal1,signal2)
        if pred:
            verification_instance.delete()
            return Response("Match",status=HTTP_200_OK)
        else:
            verification_instance.delete()
            return Response("Match Fail",status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        if verification_instance:
            verification_instance.delete()
        return Response(
            {
                "Status":"Error",
                "Error":str(e)
            },status=HTTP_400_BAD_REQUEST
        )
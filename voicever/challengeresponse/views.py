from challengeresponse.models import ChallengeResponse
from challengeresponse.serializers import ResponseSerializer
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from random import choice,randint
def generator():
    cities = [
    "New York", "London", "Paris", "Tokyo", "Mumbai",
    "Los Angeles", "Chicago", "Toronto", "Berlin", "Sydney",
    "Dubai", "Singapore", "Hong Kong", "Rome", "Barcelona",
    "Istanbul", "Moscow", "Beijing", "Seoul", "Bangkok",
    "Shanghai", "Cape Town", "São Paulo", "Mexico City", "Buenos Aires",
    "Jakarta", "Kuala Lumpur", "Amsterdam", "Vienna", "Cairo"
    ]
    boolean = ['True','False']
    a = randint(10,30)
    b = randint(10,30)
    city = choice(cities)
    boolean_value = choice(boolean)
    list_challenges = [
        [f"Say The Result Of This Expression: sum of {a} and {b} is?",f"{a+b}"],
        [f"Say: I Live In {city}",f"Say: I Live In {city}"],
        [f"Say: {boolean_value}",f"{boolean_value}"]
    ]
    return choice(list_challenges)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def challenege_view(request):
    try:
        challenge_response_output = generator()
        cha = ChallengeResponse.objects.create(
            user = request.user,
            challenge_message = challenge_response_output[0],
            response_message = challenge_response_output[1]
        )
        return Response(cha.challenge_message,status=HTTP_200_OK)
    except Exception as e:
        return Response(
            {
                "Status":"Challenge Generation Failed",
                "Error":str(e)
            },status=HTTP_400_BAD_REQUEST)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def response_view(request):
    try:
        data = request.data
        response = ResponseSerializer(data=data)
        response.is_valid(raise_exception=True)
        challenge = ChallengeResponse.objects.get(user=request.user)
        if not challenge:
            return Response("Challenge Not Assigned To User, Please Generate A Challenge",
                            status=HTTP_400_BAD_REQUEST)
        if response.validated_data['response'] == challenge.response_message:
            challenge.delete()
            return Response("Authentication Successful",status=HTTP_200_OK)
        else:
            challenge.delete()
            return Response("Authentication Not Successful",status=HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(
            {
                "Status":"Error",
                "Error":str(e)
            }
        ,status=HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializer import UserSerializer
from rest_framework.status import HTTP_401_UNAUTHORIZED,HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
@api_view(['POST'])
def create(request):
    try:
        srlzr = UserSerializer(data=request.data)
        srlzr.is_valid(raise_exception=True)
        srlzr.save()
        return Response(
            {
                "Status":"Account Created Successfully"
            },status=HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {
                "Status":"Error",
                "Error":str(e)
            },status=HTTP_400_BAD_REQUEST
        )
@api_view(['POST'])
def delete(request):
    try:
        request.user.delete()
        return Response(
            {
                "Status":"Account Deleted Successfully"
            },status=HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                "Status":"Error",
                "Error":str(e)
            },status=HTTP_401_UNAUTHORIZED
        )
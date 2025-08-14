from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED,HTTP_200_OK
@api_view(['POST'])
def create(request):
    pass
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
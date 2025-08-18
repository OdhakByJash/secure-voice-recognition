from rest_framework.serializers import Serializer,CharField
class ResponseSerializer(Serializer):
    response = CharField()
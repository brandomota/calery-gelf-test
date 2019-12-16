from rest_framework.serializers import ModelSerializer

from model.models import Object


class ObjectSerializer(ModelSerializer):

    class Meta:
        model =  Object
        fields = '__all__'
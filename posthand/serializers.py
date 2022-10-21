from rest_framework import serializers

from posthand.models import Postapi

class Postserializers(serializers.ModelSerializer):
    class Meta:
        model=Postapi
        fields='__all__'


from rest_framework import serializers
from Ecommerceapp.models import Useradd

class UseAddSerializers(serializers.ModelSerializer):
    class Meta:
        model =Useradd
        fields='__all__'
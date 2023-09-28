from django.shortcuts import render
from Ecommerceapp.models import Useradd
from Ecommerceapp.serializers import UseAddSerializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class EmployeeCurdOperation(ModelViewSet):
    queryset=Useradd.objects.all()
    serializer_class=UseAddSerializers
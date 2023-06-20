from .models import *
from rest_framework import serializers


class studentserializer(serializers.ModelSerializer):
    
    class meta:
        model=student
        fields='__all__'
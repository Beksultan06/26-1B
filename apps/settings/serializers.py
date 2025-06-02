from rest_framework import serializers
from apps.settings.models import Base

class BaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'title', 'description', 'image']
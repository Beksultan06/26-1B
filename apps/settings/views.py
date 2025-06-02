from django.shortcuts import render
from rest_framework import viewsets, mixins

from apps.settings.models import Base
from apps.settings.serializers import BaseSerializers

class BaseAPI(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin
                ):
    queryset = Base.objects.all()
    serializer_class = BaseSerializers
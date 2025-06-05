from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.settings.models import Base
from apps.settings.serializers import BaseSerializers
from apps.settings.pagination import BasePagination

class BaseAPI(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin
                ):
    queryset = Base.objects.all()
    serializer_class = BaseSerializers
    pagination_class = BasePagination 

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['is_active']
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'title', 'created_at']
    ordering = ['-created_at']
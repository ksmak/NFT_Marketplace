from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from abstracts.mixins import (
    ObjectMixin,
    ResponseMixin,
    ErrorMixin
)
from abstracts.paginators import NumberPaginator
from .models import PublicNFT
from .serializers import PublicNFTSerializer


class PublicNFTViewSet(ViewSet, ObjectMixin, ResponseMixin, ErrorMixin):
    """
        View set for public NFT
    """
    queryset = PublicNFT.objects.all()
    permission_classes = [IsAuthenticated]
    paginator = NumberPaginator

    def list(self, request):
        queryset = PublicNFT.objects.all()
        serializer = PublicNFTSerializer(queryset, many=True)
        return self.get_json_response(serializer.data, self.paginator())

    def create(self, request):
        serializer = PublicNFTSerializer(data=request.data)

        if not serializer.is_valid():
            return self.get_json_error(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return self.get_json_response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.get_object(self.queryset, pk)

        if not obj:
            return self.get_json_error(
                'NFT not found.',
                status.HTTP_404_NOT_FOUND
            )

        serializer = PublicNFTSerializer(obj)

        return self.get_json_response(serializer.data)

    def _update(self, request, pk=None):
        obj = self.get_object(self.queryset, pk)

        if not obj:
            return self.get_json_error(
                'NFT not found.',
                status.HTTP_404_NOT_FOUND
            )

        if request.user != obj.user:
            return self.get_json_error(
                'User not owner NFT.',
                status.HTTP_400_BAD_REQUEST
            )

        serializer = PublicNFTSerializer(
            instance=obj,
            data=request.data
        )

        if not serializer.is_valid():
            return self.get_json_error(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return self.get_json_response(serializer.data)

    def update(self, request, pk=None):
        return self._update(request, pk)

    def partial_update(self, request, pk=None):
        return self._update(request, pk)

    def destroy(self, request, pk=None):
        obj = self.get_object(self.queryset, pk)

        if not obj:
            return self.get_json_error(
                'NFT not found.',
                status.HTTP_404_NOT_FOUND
            )

        if request.user != obj.user:
            return self.get_json_error(
                'User not owner NFT.',
                status.HTTP_400_BAD_REQUEST
            )

        obj.delete()

        return self.get_json_response('NFT deleted.')

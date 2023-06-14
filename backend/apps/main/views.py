from datetime import datetime
from django.conf import settings

from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action

from abstracts.mixins import (
    ObjectMixin,
    ResponseMixin,
    ErrorMixin
)
from abstracts.paginators import CustomNumberPagination
from .serializers import ArtSerializer
from settings.nft_service import ArtCollection

art = ArtCollection(
    network=settings.ETH_NETWORK,
    account_address=settings.ETH_ACCOUNT_ADDRESS,
    private_key=settings.ETH_PRIVATE_KEY,
    contract_file=settings.ETH_CONTRACT_FILE,
    contract_address=settings.ETH_CONTRACT_ADDRESS
)


class PublicNFTViewSet(ViewSet, ObjectMixin, ResponseMixin, ErrorMixin):
    """
        View set for public NFT
    """
    permission_classes = [IsAuthenticated]
    pagination_class = CustomNumberPagination
    queryset = art.get_all_nft()

    def list(self, request):
        serializer = ArtSerializer(data=self.queryset, many=True)

        if not serializer.is_valid():
            return self.get_json_error(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        paginator = self.pagination_class()
        paginator.paginate_queryset(self.queryset, request)
        return self.get_json_response(serializer.data)

    @action(detail=False, methods=['POST'])
    def create_nft(self, request):
        self.request.data['status'] = ArtCollection.STATUS_FOR_SALE
        self.request.data['date_of_creation'] = datetime.now().strftime(
            "%m.%d.%Y %H:%M:%S")

        serializer = ArtSerializer(data=self.request.data)

        if not serializer.is_valid():
            return self.get_json_error(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        receipt = art.create_nft(**serializer.data)

        if receipt['status'] != 1:
            return self.get_json_response({
                'result': (f'Transaction failed: '
                           f'{receipt["transactionHash"].hex()}')
            }, status.HTTP_400_BAD_REQUEST)

        return self.get_json_response('success')

    @action(detail=False, methods=['POST'])
    def buy_nft(self, request):
        serializer = ArtSerializer(data=self.request.data)

        if not serializer.is_valid():
            return self.get_json_error(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        receipt = art.buy_nft(**serializer.data)

        if receipt['status'] != 1:
            return self.get_json_response({
                'result': (f'Transaction failed: '
                           f'{receipt["transactionHash"].hex()}')
            }, status.HTTP_400_BAD_REQUEST)

        return self.get_json_response('success')

    def retrieve(self, request, pk=None):
        obj = self.get_object(self.queryset, pk)

        if not obj:
            return self.get_json_error(
                'NFT not found.',
                status.HTTP_404_NOT_FOUND
            )

        serializer = ArtSerializer(obj)

        return self.get_json_response(serializer.data)

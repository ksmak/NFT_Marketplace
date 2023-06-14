from rest_framework import serializers


class ArtSerializer(serializers.Serializer):
    """
        Art (NFT object) serializer.
    """
    status = serializers.IntegerField(required=False)
    uri = serializers.CharField()
    owner = serializers.CharField()
    price = serializers.IntegerField()
    date_of_creation = serializers.CharField(required=False)
    title = serializers.CharField()


class BuyArtSerializer(serializers.Serializer):
    """
        Serializer for buying Art(NFT object)
    """
    buyer = serializers.CharField()
    tokenId = serializers.IntegerField()
    markup = serializers.IntegerField()

from rest_framework import serializers

from .models import PublicNFT, Transaction


class PublicNFTSerializer(serializers.ModelSerializer):
    """
        Public NFT serializer.
    """
    class Meta:
        model = PublicNFT
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    """
        Transaction serializer.
    """
    class Meta:
        model = Transaction
        fields = '__all__'

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class PublicNFT(models.Model):
    """
        Public NFT model.
    """
    token_id = models.IntegerField(
        verbose_name='token id',
        unique=True,
        primary_key=True
    )
    image = models.ImageField(
        verbose_name='image',
        upload_to=upload_to
    )

    class Meta:
        verbose_name = 'public NFT'
        verbose_name_plural = 'public NFTs'

    def __str__(self) -> str:
        self.token

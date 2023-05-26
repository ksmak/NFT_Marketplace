from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class PublicNFT(models.Model):
    """
        Public NFT model.
    """
    token = models.CharField(
        verbose_name='token',
        max_length=258,
        unique=True,
        primary_key=True
    )
    user = models.ForeignKey(
        verbose_name='user',
        to=User,
        on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField(
        verbose_name='amount',
        default=0
    )
    date_of_creation = models.DateTimeField(
        verbose_name='date of creation',
        auto_now_add=True
    )
    date_of_change = models.DateTimeField(
        verbose_name='date of change',
        auto_now=True
    )

    class Meta:
        verbose_name = 'public NFT'
        verbose_name_plural = 'public NFTs'

    def __str__(self) -> str:
        self.token


class Transaction(models.Model):
    """
        Transaction model.
    """
    from_user = models.ForeignKey(
        verbose_name='from user',
        to=User,
        on_delete=models.RESTRICT,
        related_name='from_user'
    )
    to_user = models.ForeignKey(
        verbose_name='to user',
        to=User,
        on_delete=models.RESTRICT,
        related_name='to_user'
    )
    token = models.CharField(
        verbose_name='token',
        max_length=258
    )
    amount = models.PositiveIntegerField(
        verbose_name='amount',
        default=0
    )
    date_of_creation = models.DateTimeField(
        verbose_name='date of creation',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    def __str__(self) -> str:
        return (
            f"Transaction: {self.id}, date: {self.date_of_creation}, "
            f"token={self.token}, amount={self.amount}"
        )

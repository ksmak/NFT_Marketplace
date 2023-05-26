from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import (
    CreateUserSerializer
)


class RegisterUserView(APIView):
    """
        View for register new user
    """
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        serializer = CreateUserSerializer(
            data=request.data
        )

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        if get_user_model().objects.filter(
                                            email=request.data.get('email')
                                          ).exists():
            return Response(
                {
                    'error': 'User already exists.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        user = serializer.create()
        return Response(
            {
                'activate_code': user.activate_code
            },
            status=status.HTTP_201_CREATED
        )


class ActivateUserView(APIView):
    """
        View for activate new user by email
    """
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        activate_code = request.query_params.get('code')
        if not activate_code:
            return Response(
                {
                    'error': 'Bad request'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user = get_user_model().objects.filter(
            activate_code=activate_code
        ).first()

        if not user:
            return Response(
                {
                    'error': 'User not found.'
                },
                status=status.HTTP_404_NOT_FOUND
            )

        user.is_active = True
        user.save(update_fields=('is_active', 'activate_code'))
        return Response(
            {
                'result': 'User activated'
            },
            status=status.HTTP_200_OK
        )

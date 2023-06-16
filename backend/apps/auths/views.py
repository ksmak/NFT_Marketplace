from django.contrib.auth import get_user_model

from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    MyTokenObtainPairSerializer,
    UserSerializer,
    CreateUserSerializer,
)

from abstracts.mixins import ObjectMixin, ResponseMixin, ErrorMixin


User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(ViewSet, ObjectMixin, ResponseMixin, ErrorMixin):
    """
        ViewSet for user model
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        obj = self.get_object(self.queryset, pk)

        if not obj:
            return self.get_json_error(
                'User not found.',
                status.HTTP_404_NOT_FOUND
            )

        if obj.id != request.user.id:
            return self.get_json_error(
                'User is not self.',
                status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(obj)

        return self.get_json_response(serializer.data)

    def update(self, request, pk=None):
        return self._update(request, pk)

    def partial_update(self, request, pk=None):
        return self._update(request, pk, partial=True)

    def _update(self, request, pk=None, partial=None):
        obj = self.get_object(self.queryset, pk)

        if not obj:
            return self.get_json_error(
                'User not found.',
                status.HTTP_404_NOT_FOUND
            )

        if obj.id != request.user.id:
            return self.get_json_error(
                'User is not self.',
                status.HTTP_400_BAD_REQUEST
            )

        serializer = UserSerializer(obj, data=request.data, partial=partial)

        if not serializer.is_valid():
            return self.get_json_error(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return self.get_json_response('Success update')

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        serializer = CreateUserSerializer(
            data=request.data
        )

        if not serializer.is_valid():
            return self.get_json_error(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        user = serializer.create()

        return self.get_json_response(user.activate_code)

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def activate(self, request):
        activate_code = request.data.get('activate_code')

        if not activate_code:
            return self.get_json_error(
                'Activation code not exist',
                status.HTTP_400_BAD_REQUEST
            )

        user = get_user_model().objects.filter(
            activate_code=activate_code
        ).first()

        if not user:
            return self.get_json_error(
                'User not found.',
                status.HTTP_404_NOT_FOUND
            )

        user.is_active = True

        user.save(update_fields=('is_active', 'activate_code'))

        return self.get_json_response('User activated')

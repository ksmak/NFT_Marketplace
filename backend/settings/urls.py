from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from auths.views import (
    RegisterUserView,
    ActivateUserView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # noqa
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # noqa
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/user/register/', RegisterUserView.as_view()),
    path('api/user/activate/', ActivateUserView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

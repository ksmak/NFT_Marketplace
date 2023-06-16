from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenRefreshView

from auths.views import (
    MyTokenObtainPairView,
    UserViewSet,
)
from main.views import PublicNFTViewSet

router = SimpleRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'public_nft', PublicNFTViewSet, basename='public_nft')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', MyTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

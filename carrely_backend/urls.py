from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/carrels/', include('carrels.urls')),
    #path('api/feed/', include('feed.urls')),
    path('api/gamification/', include('gamification.urls')),
    #path('api/social/', include('social.urls')),

    # API Documentation
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(), name="swagger-ui"),
]

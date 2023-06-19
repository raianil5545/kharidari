from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path("", include("accounts.urls")),
     path('docs/', include_docs_urls(title='KharidariApi')),
     path('schema', get_schema_view(
        title="KharidariApi",
        description="API for the KharidariApi",
        version="1.0.0"
    ), name='openapi-schema'),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
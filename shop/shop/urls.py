from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from tool.views import product_list, product_details_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name="product_list"),
    path(
        'product/<int:product_id>/', product_details_view, name="product_details_view"
    ),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
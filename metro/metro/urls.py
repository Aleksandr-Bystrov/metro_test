from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from users.views import RegisrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('auth/registration/', RegisrationView.as_view(), name='registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

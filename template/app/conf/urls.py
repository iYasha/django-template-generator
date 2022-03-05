from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from rest_framework.routers import SimpleRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from accounts import urls as account_urls
from drf_yasg import openapi


handler500 = 'base.handlers.handler500'
handler404 = 'base.handlers.handler404'


class OptionalSlashRouter(SimpleRouter):

    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
schema_view = get_schema_view(
    openapi.Info(
        title="{&PROJECT_NAME&}",
        default_version='v1',
        description="{&PROJECT_DESCRIPTION&}",
        contact=openapi.Contact(email="{&PROJECT_CONTACT_EMAIL&}"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

routes_list = [
    account_urls.route_list,
]

for routes in routes_list:
    for route in routes:
        router.register(route[0], route[1])

urlpatterns = [
    url(r'^admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^', include(router.urls)),
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]

# Serve static
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, }),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]

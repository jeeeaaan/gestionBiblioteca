from django.urls import include, path

from .routers import router

urlpatterns = [
    path("api-jean-v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
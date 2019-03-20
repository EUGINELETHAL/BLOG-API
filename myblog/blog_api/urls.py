from django.urls import re_path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ArticleViewSet, LoginView

app_name = "blog_api"

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
   re_path(r'^', include(router.urls)),
   re_path (r'^auth/login$', LoginView.as_view())

]
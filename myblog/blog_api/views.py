
from django.contrib.auth import authenticate, login

from rest_framework import viewsets, status
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Article
from .serializers import CategorySerializer, ArticleSerializer, UserSerializer


#........
class CategoryViewSet(viewsets.ModelViewSet):
    """
    Allow for CRUD functionality for a category resource
    Request methods (api/v1/categories): POST, GET
    Request methods (api/v1/categories/<id>): GET, PUT, DELETE
    """
    # [WIP] Permissions
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Allow for CRUD functionality for a article resource
    Request methods (api/v1/articles): POST, GET
    Request methods (api/v1/articles/<id>): GET, PUT, DELETE
    """
    # [WIP] Permissions
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

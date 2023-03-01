from rest_framework import routers
from .api import BookViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='Book')
router.register('authors', AuthorViewSet, basename='Author')
urlpatterns = router.urls


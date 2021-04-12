from django.urls import path, include
from .views import ArticleViewSet 
#ArticleList, ArticleDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('', include(router.urls)),
    #path('articles/', ArticleList.as_view()),
    #path('articles/<int:id>', ArticleDetails.as_view()),
    #path('articles/', article_list),
    #path('articles/<int:pk>', article_details),
]

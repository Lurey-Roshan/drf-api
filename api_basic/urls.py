from django.urls import path, include
from .views import article_list, article_detail,ArticleView,ArticleDetails,GenericAPIView,ArticleViewSet,Article_viewSet,Article_ViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSet, basename='article')
router.register('articles',Article_viewSet, basename='articles')
router.register('articless',Article_ViewSet, basename='articless')

urlpatterns = [
	path('viewset/', include(router.urls)),
	path('viewset/<int:pk>/', include(router.urls)),
 
    #path('article/',article_list),
    #path('article/',ArticleView.as_view()),
    path('generic/article/<int:id>',GenericAPIView.as_view()),
    #path('article/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view())
]
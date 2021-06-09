from django.urls import path
from .views import article_list, article_detail,ArticleView,ArticleDetails,GenericAPIView
urlpatterns = [
 
    #path('article/',article_list),
    #path('article/',ArticleView.as_view()),
    path('generic/article/<int:id>',GenericAPIView.as_view()),
    #path('article/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetails.as_view())
]
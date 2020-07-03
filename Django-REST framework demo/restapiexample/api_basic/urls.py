from django.urls import path, include
from . views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticleViewSet, basename='article')
urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail_view),
    path('generic/article/<int:id>/', GenericApiView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view(),),
    path('generic/article/', GenericApiView.as_view()),

]
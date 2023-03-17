from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]


# urlpatterns = [
#     path('v1/jwt/create/',
#          TokenObtainPairView.as_view(),
#          name='token_obtain_pair'),
#     path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
#     path('v1/', include(router.urls)),
# ]

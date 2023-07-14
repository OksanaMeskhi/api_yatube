from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import GroupViewSet, PostViewSet, CommentViewSet


v1_router = DefaultRouter()

v1_router.register(
    prefix='groups',
    viewset=GroupViewSet,
    basename='groups',
)
v1_router.register(
    prefix='posts',
    viewset=PostViewSet,
    basename='posts',
)
v1_router.register(
    prefix=r'posts/(?P<post_id>\d+)/comments',
    viewset=CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import (
    permissions,
    status,
    filters,
    viewsets,
)
from . serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer,
    FollowSerializer
)

from .permissions import IsAuthorOrReadOnly
from posts.models import Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

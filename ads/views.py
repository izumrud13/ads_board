from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.filters import AdFilter
from ads.models import Comment, Ad
from ads.paginations import CustomPagination
from ads.permissions import IsOwner, IsAdmin
from ads.serializers import CommentSerializers, AdSerializers, AdDetailSerializers


# Create your views here.
class AdListApiView(generics.ListAPIView):
    """Просмотр всех объявлений"""
    serializer_class = AdSerializers
    queryset = Ad.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)  # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter  # Выбираем созданный фильтр


class AdCreateApiView(generics.CreateAPIView):
    """Создание объявления"""
    serializer_class = AdDetailSerializers
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для автоматческой привязки объявления к пользователю"""
        serializer.save(author=self.request.user)


class AdUpdateApiView(generics.UpdateAPIView):
    """Редактирование объявления"""
    serializer_class = AdDetailSerializers
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class AdRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр объявления"""
    serializer_class = AdDetailSerializers
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]


class AdDestroyApiView(generics.DestroyAPIView):
    """Удаление объявлений"""
    serializer_class = AdDetailSerializers
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class UserAdListApiView(generics.ListAPIView):
    """Просмотр объявлний текущего пользовтаеля"""
    serializer_class = AdDetailSerializers
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentListApiView(generics.ListAPIView):
    """Просмотр всех отзывов"""
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
    permission_classes = [AllowAny]


class CommentCreateApiView(generics.CreateAPIView):
    """Создание отзыва"""
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для автоматичесой привязки пользователя к отзыву"""
        ad_pk = self.kwargs.get('ad_pk')
        ad_for_comment = Ad.objects.get(pk=ad_pk)
        comment_pk = self.kwargs.get('pk')
        serializer.save(author=self.request.user, ad=ad_for_comment, pk=comment_pk)


class CommentUpdateApiView(generics.UpdateAPIView):
    """Редактирование отзыва"""
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class CommentDestroyApiView(generics.DestroyAPIView):
    """Удаление отзыва"""
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]

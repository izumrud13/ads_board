from django.urls import path

from ads.apps import AdsConfig
from ads.views import CommentCreateApiView, CommentListApiView, CommentUpdateApiView, CommentDestroyApiView, \
    AdListApiView, AdCreateApiView, AdUpdateApiView, AdRetrieveApiView, AdDestroyApiView, UserAdListApiView


app_name = AdsConfig.name

urlpatterns = [
    path('', AdListApiView.as_view(), name='notices_list'),
    path('create/', AdCreateApiView.as_view(), name='notices_create'),
    path('update/<int:pk>/', AdUpdateApiView.as_view(), name='notices_update'),
    path('detail/<int:pk>/', AdRetrieveApiView.as_view(), name='notices_detail'),
    path('delete/<int:pk>/', AdDestroyApiView.as_view(), name='notices_delete'),
    path('me_list/', UserAdListApiView.as_view(), name='notices_list'),
    path('create/<ad_pk>/', CommentCreateApiView.as_view(), name='review_create'),
    path('list/', CommentListApiView.as_view(), name='review_list'),
    path('update/<int:pk>/', CommentUpdateApiView.as_view(), name='review_update'),
    path('delete/<int:pk>/', CommentDestroyApiView.as_view(), name='review_delete'),
]
from django.urls import path
from .views import PostCreate
from .views import TagCreate
from .views import PostDetail
from .views import TagDetail
from .views import TagUpdate
from .views import PostUpdate
from .views import TagDelete
from .views import PostDelete
from .views import posts_list
from .views import tags_list


urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url')]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from  import Post, PostView, Like, Comment

from posts.views import(
    PostDeleteView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', PostListView.as_view(),name='list'),
    path('create/', PostCreateView.as_view(),name='create'),
    path('<slug>', PostDetailView.as_view(),name='datail'),
    path('<slug>/update/', PostUpdateView.as_view(),name='update'),
    path('<slug>/delete/', PostDeleteView.as_view(),name='delete')  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from .views import index,contact,service,projects
from blog.views import PostListView, PostDetailView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    # path('resume/', resume, name='resume'),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('projects/', projects, name='projects'),
    path('service/', service, name='service'),
]

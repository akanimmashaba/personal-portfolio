
from django.urls import path,include
from .views import index,projects
from blog.views import PostListView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('projects/', projects, name='projects'),
]

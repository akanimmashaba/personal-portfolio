
from django.urls import path
from .views import index,contact,service,resume,ListPosts,projects


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    # path('resume/', resume, name='resume'),
    path('blog/', ListPosts, name='blog'),
    path('projects/', projects, name='projects'),
    path('service/', service, name='service'),
]

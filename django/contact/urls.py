
from django.urls import path
from . import views

app_name = 'contact'


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.contact, name='contact'),
]

from django.urls import path, include
from django.views.generic import RedirectView

from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index')

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superheroes/', include('superheroes.urls')),
    path('', RedirectView.as_view(url='/superheroes'))
]
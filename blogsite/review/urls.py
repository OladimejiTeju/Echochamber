from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
from . import models
import urllib


urlpatterns = [
    #path('', views.index, name='index'),
	path('', views.IndexView.as_view(), name='index'),
	path('<title>', views.detail, name='detail'),
	
	 
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
# urlpatterns += staticfiles_urlpatterns()

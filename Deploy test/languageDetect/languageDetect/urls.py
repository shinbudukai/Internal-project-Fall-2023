
from languageDetectApp.views import GetAllLanguageAPIView #, HomepageView
from django.contrib import admin
from django.urls import path, include
from languageDetectApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.HomepageView.as_view(), name='app' ),
    path('', views.getInput),
    path('api/', GetAllLanguageAPIView.as_view(), name='app' ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
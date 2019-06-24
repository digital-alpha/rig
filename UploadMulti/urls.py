from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'UploadMulti'

urlpatterns = [
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    url(r'^drag-and-drop-upload/$', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
    path('analysis/<int:pk>', views.analysis, name='analysis'),
    url(r'^csv/$', views.csv, name='csv'),
    url(r'^form_post/$', views.form_post, name='form_post'),
    path('process/', views.process, name='process'),
    path('save/', views.save_info, name='save_info'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

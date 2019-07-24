from django.urls import path, include
from .api_views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', DocumentViewset)
router2 = routers.DefaultRouter()
router2.register('', DetailViewset)

urlpatterns = [

    path('document/', include(router.urls)),
    path('detail/', include(router2.urls)),
    path('process/', processAPI),
    path('process/<int:pk>', processApiSingle),
    path('clear/', clearAPI),
    path('detail/<int:pk>', infoAPI),

] 


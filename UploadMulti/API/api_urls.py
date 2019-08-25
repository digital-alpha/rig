from django.urls import path, include
from .api_views import *

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('', DocumentViewset)
router2 = routers.DefaultRouter()
router2.register('', DetailViewset)
router3 = routers.DefaultRouter()
router3.register('', RoleViewset)

urlpatterns = [

    path('document/', include(router.urls)),
    path('detail/', include(router2.urls)),
    path('process/', processAPI),
    path('process/<int:pk>', processApiSingle),
    path('clear/', clearAPI),
    path('excel/', excelAPI),
    path('displacy/<int:pk>', DisplacyAPI),
    path('clear/<int:pk>', clearSingleApi),
    path('detail/<int:pk>', infoAPI),
    path('role/', include(router3.urls)),


    path('api-token-auth/', obtain_auth_token, name='api_token_auth')

] 


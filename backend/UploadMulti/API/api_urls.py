from django.urls import path, include
from .api_views import *

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token	

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
    path('current_user/', current_user),
    path('api-token-auth/', obtain_jwt_token, name='api_token_auth'),
    path('form_post/', form_post),
] 


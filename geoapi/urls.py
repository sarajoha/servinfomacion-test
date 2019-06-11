from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'crear', views.UserViewSet)
router.register(r'lista', views.GroupViewSet)
router.register(r'usuario', views.GroupViewSet)
router.register(r'eliminar', views.GroupViewSet)
router.register(r'geocodificar_base', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

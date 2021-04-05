from django.urls import include, path
from rest_framework import routers
from . import views


# The REST Framework router will make sure our requests end up at the right resource dynamically.
# If we add or delete items from the database, the URLs will update to match.
router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'spells', views.SpellViewSet)

# Wire up the API using automatic URL routing.
# Additionally, include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
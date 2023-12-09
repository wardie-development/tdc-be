from .views import BrandViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)

urlpatterns = router.urls

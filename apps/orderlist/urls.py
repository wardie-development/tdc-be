from .views import CellphoneModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"order-list", CellphoneModelViewSet)

urlpatterns = router.urls

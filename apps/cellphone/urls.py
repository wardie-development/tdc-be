from .views import CellphoneViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cellphones', CellphoneViewSet)

urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from sale import viewsets

router = DefaultRouter()
router.register('marital_status', viewsets.MaritalStatusViewSet)
router.register('department', viewsets.DepartmentViewSet)

urlpatterns = router.urls

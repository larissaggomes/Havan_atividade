from rest_framework.routers import DefaultRouter
from sale import viewsets

router = DefaultRouter()
router.register('marital_status', viewsets.MaritalStatusViewSet)
router.register('department', viewsets.DepartmentViewSet)
router.register('State', viewsets.StateViewSet)
router.register('city', viewsets.CityViewSet)
router.register('zone', viewsets.ZoneViewSet)
router.register('employee', viewsets.EmployeeViewSet)
router.register('customer', viewsets.CustomerViewSet)
router.register('district', viewsets.DistrictViewSet)
router.register('branch', viewsets.BranchViewSet)
router.register('product', viewsets.ProductViewSet)
router.register('product_group', viewsets.ProductGroupViewSet)
router.register('supplier', viewsets.SupplierViewSet)
router.register('sale', viewsets.SaleViewSet)
router.register('sale_product', viewsets.SaleProductViewSet)

urlpatterns = router.urls

from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "TDC Administrativo"
admin.site.site_title = "TDC Administrativo"
admin.site.index_title = "TDC Administrativo"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.cellphone.urls")),
    path("api/v1/", include("apps.orderlist.urls")),
]

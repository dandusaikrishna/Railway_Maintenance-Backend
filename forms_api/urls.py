from django.urls import path
from . import views

urlpatterns = [
    path('api/forms/bogie-checksheet', views.BogieChecksheetView.as_view(), name='bogie-checksheet'),
    path('api/forms/wheel-specifications', views.WheelSpecificationPostView.as_view(), name='wheel-specifications-post'),
    path('api/forms/wheel-specifications/list', views.WheelSpecificationGetView.as_view(), name='wheel-specifications-get'),
]

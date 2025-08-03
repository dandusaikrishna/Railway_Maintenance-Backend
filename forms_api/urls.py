from django.urls import path
from . import views
from .views import LoginView

urlpatterns = [
    path('api/users/login/', LoginView.as_view(), name='login'),
    path('api/forms/bogie-checksheet', views.BogieChecksheetView.as_view(), name='bogie-checksheet'),
    path('api/forms/wheel-specifications', views.WheelSpecificationPostView.as_view(), name='wheel-specifications-post'),
    path('api/forms/wheel-specifications/list', views.WheelSpecificationGetView.as_view(), name='wheel-specifications-get'),
]

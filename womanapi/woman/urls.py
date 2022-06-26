from django.urls import path
from .views import WomanAPIView, UserAPIView



urlpatterns = [
    path('v1/womanlist/', WomanAPIView.as_view({'get': 'list'})),
    path('v1/womanlist/create/', WomanAPIView.as_view({'post': 'create'})),
    path('v1/userlist/', UserAPIView.as_view({'get': 'list'})),
]    
    
    
    



    
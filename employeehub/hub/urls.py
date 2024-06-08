from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name='home'),
    
    # Department URLs
    path('dept/', DepartmentListView.as_view(), name='department_list'),
    path('create/', DepartmentCreateView.as_view(), name='department_create'),
    path('update/<int:pk>/', DepartmentUpdateView.as_view(), name='department_update'),
    path('department/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),
]



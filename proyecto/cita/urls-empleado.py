from django.urls import path, include
from . import views

urlpatterns = [
    # get and post req. for insert operation
    path('', views.empleado_form, name='empleado_insert'),
    # get and post req. for update operation
    path('<int:id>/', views.empleado_form, name='empleado_update'),
    path('delete/<int:id>/', views.empleado_delete, name='empleado_delete'),
    # get req. to retrieve and display all records
    path('list/', views.empleado_list, name='empleado_list')
]

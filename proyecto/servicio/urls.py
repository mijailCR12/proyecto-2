from django.urls import path, include
from . import views

urlpatterns = [
    # get and post req. for insert operation
    path('', views.servicio_form, name='servicio_insert'),
    # get and post req. for update operation
    path('<int:id>/', views.servicio_form, name='servicio_update'),
    path('delete/<int:id>/', views.servicio_delete, name='servicio_delete'),
    # get req. to retrieve and display all records
    path('list/', views.servicio_list, name='servicio_list')
]

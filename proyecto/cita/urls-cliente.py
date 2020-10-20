from django.urls import path, include
from . import views

urlpatterns = [
    # get and post req. for insert operation
    path('', views.cliente_form, name='cliente_insert'),
    # get and post req. for update operation
    path('<int:id>/', views.cliente_form, name='cliente_update'),
    path('delete/<int:id>/', views.cliente_delete, name='cliente_delete'),
    # get req. to retrieve and display all records
    path('list/', views.cliente_list, name='cliente_list')
]

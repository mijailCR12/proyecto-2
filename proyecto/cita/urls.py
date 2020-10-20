from django.urls import path, include
from . import views

urlpatterns = [
    # get and post req. for insert operation
    path('', views.cita_form, name='cita_insert'),
    # get and post req. for update operation
    path('<int:id>/', views.cita_form, name='cita_update'),
    path('delete/<int:id>/', views.cita_delete, name='cita_delete'),
    # get req. to retrieve and display all records
    path('list/', views.cita_list, name='cita_list')
]

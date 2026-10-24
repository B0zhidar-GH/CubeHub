from django.urls import path

#from cubehub.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.solve_list, name='solve_list'),
    path('<int:solve_id>/edit/', views.solve_edit, name='solve_edit'),
    path('<int:solve_id>/delete/', views.solve_delete, name='solve_delete'),
    path('<int:solve_id>/details/', views.solve_details, name='solve_details')
]

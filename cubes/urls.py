from django.urls import path
from . import views

urlpatterns = [
    path('', views.cube_list, name='cube_list'),

    path('<int:cube_id>/edit/', views.cube_edit, name='cube_edit'),

    path('<int:cube_id>/delete/', views.cube_delete, name='cube_delete')
]
from django.urls import path

#from cubehub.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.cuber_list, name='cuber_list'),
    path('<int:cuber_id>/edit/', views.cuber_edit, name='cuber_edit'),

    path('<int:cuber_id>/delete/', views.cuber_delete, name='cuber_delete')
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.create),
    path('create',views.create),
    path('show',views.show),
    path('update/<int:id>',views.update),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.dlt)

]
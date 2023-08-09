from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
   path('', views.index),
   path('Save_Student_Information', views.save_stu_info),
   path('ID_Card', views.id_card),
   path('Delete_Record', views.delete_rec),
   path('ic', views.ic)

]

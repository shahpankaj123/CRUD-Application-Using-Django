from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Update/',views.update,name='update'),
    path('Add/',views.add,name='add'),
    path('Delete1/<id>',views.delete1,name='delete1'),
    path('Delete',views.delete,name='delete'),
    
    
    
]
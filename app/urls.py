from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Update/',views.update,name='update'),
    path('Update1/',views.update1,name='update1'),
    path('Add/',views.add,name='add'),
    path('Delete1/<id>',views.delete1,name='delete1'),
    path('Delete',views.delete,name='delete'),
    
    
    
]
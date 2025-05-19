from django.urls import path 
from .import views

#locolhost:8000/chai
#localhost:8000/chai/order
#
urlpatterns = [
    path('',views.all_drawings,name='all_drawings'),
    path('<int:drawing_id>/',views.drawing_detail,name='drawing_detail'),
    path('add/', views.add_drawing, name='add_drawing'),
    path('success/', views.success_page, name='drawing_success'), 
    path('<int:drawing_id>/edit/', views.edit_drawing, name='edit_drawing'),
    path('delete/<int:drawing_id>/', views.delete_drawing, name='delete_drawing'),


    
]
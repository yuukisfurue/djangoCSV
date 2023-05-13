from django.urls import path
from . import views
from .views import GuestList
from .views import GuestDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('list', GuestList.as_view()), #☆
    path('detail/<int:pk>', GuestDetail.as_view()), #☆
    path('find', views.find, name='find'), 
    path('<int:num>', views.index, name='index'),
    path('export/', views.csv_export, name='csv_export'),
]
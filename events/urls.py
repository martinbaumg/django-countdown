from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addevent', views.addevent, name='addevent'),
    path('deleteevent/<int:id>', views.deleteevent, name='delete-event'),
    path('showevent/<int:id>', views.showevent, name='show-event'),
    path('editevent/<int:id>', views.editevent, name='edit-event'),
    path('allevents', views.allevents, name='all-events'),
]
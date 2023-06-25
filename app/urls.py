from django.urls import path
from.import views
urlpatterns = [
    path('',views.index),
    path('song/',views.get),
]
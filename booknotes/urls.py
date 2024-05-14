from django.urls import path
from . import views

urlpatterns=[
    path('',views.getRoutes,name="routes"),
    path('notes/',views.getNotes, name="notes"),
    path('notes/<str:currId>',views.getNote, name="note")
]
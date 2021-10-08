from django.urls import path
from books import views

urlpatterns=[
    path('add/',views.add_book, name='bookadd')
]

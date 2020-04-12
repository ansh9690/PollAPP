from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('list/', views.all_polls, name='all_polls'),
    path('create/', views.create_poll, name='create_poll'),
    path('result/<int:result_id>/', views.result, name='result'),
    path('vote/<int:vote_id>/', views.vote, name='vote'),
]

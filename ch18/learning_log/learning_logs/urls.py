"""Define the URL pattern of learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Detailed pages for specific topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]

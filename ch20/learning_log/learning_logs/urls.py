"""Define learning_logs pattern"""


from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Show all topics
    path('topics/', views.topics, name='topics'),
    # Detailed pages for specific topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # A page for adding a new theme
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page for editing entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

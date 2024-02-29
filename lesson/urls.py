from django.urls import path

from lesson.views import LessonsListView

app_name = 'lesson'

urlpatterns = [
    path('', LessonsListView.as_view(), name='lessons_list'),
]

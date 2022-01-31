from django.urls import path
from api import views

urlpatterns = [
  path('tasks/', views.TaskListApiView.as_view()),
  path('tasks/<int:task_id>', views.TaskDetailApiView.as_view()),
  path('lanes/', views.LaneListApiView.as_view()),
  path('lanes/<int:lane_id>', views.LaneDetailApiView.as_view()),
  path('lanes/<int:lane_id>/tasks', views.TaskLaneListApiView.as_view()),
  path('user/', views.UserCreateApiView.as_view()),
  path('user/<str:user_id>', views.UserInfoApiView.as_view()),
  path('user/<str:user_id>/tasks', views.UserTaskInfoApiView.as_view()),
  path('user/<str:user_id>/lanes', views.UserLaneInfoApiView.as_view()),
]
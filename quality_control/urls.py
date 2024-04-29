from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index),
    path('bug_list/', views.bug_list, name='bug_list'),
    path('feature_list/', views.feature_list, name='feature_list'),
   # path('bug/<int:bug_id>/', views.bug_detail),
   # path('feature/<int:feature_id>/', views.feature_id_detail),
    path('bug/<int:bug_id/>', views.BugDetailView.as_view(), name='bug_detail'),
    path('feature/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_id_detail'),

]
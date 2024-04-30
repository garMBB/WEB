from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
# path('', views.index),
    path('', views.IndexView.as_view(), name='index'),
    path('bug_list/', views.bug_list, name='bug_list'),
    path('feature_list/', views.feature_list, name='feature_list'),
    path('bug_list/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('bug_list/add_bug', views.add_bug, name='add_bug'),
    path('feature_list/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('feature_list/add_feature', views.add_feature, name='add_feature'),

]
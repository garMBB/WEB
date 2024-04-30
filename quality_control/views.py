from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BugReportForm
from .forms import FeatureRequestForm
# Create your views here.

#def index(request):
#    bug_list_url = reverse('quality_control:bug_list')
#    feature_list_url = reverse('quality_control:feature_list')
#    html = f"<h1>Cистема контроля качества</h1><a href='{bug_list_url}'>Посмотреть список всех багов</a><br><a href='{feature_list_url}'>Перейти к запросам на улучшение</a>"
#    return HttpResponse(html)

#class IndexView(View):
#    def get(self, request, *args, **kwargs):
#        bug_list_url = reverse('quality_control:bug_list')
#        feature_list_url = reverse('quality_control:feature_list')
#        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Посмотреть список всех багов</a><br><a href='{feature_list_url}'>Перейти к запросам на улучшение</a>"
#        return HttpResponse(html)

def index(request):
    return render(request, 'quality_control/index.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


#def bug_list(request, bug_id):
#    bugs = BugReport.objects.all()
#    bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
#    for bug in bugs:
#        bugs_html += f'<li><a href="{bug_id}/">{bug.title}</a> - {bug.status}</li>'
#    bugs_html += '</ul>'
#    return HttpResponse(bugs_html)

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

#def feature_list(request):
#   features = FeatureRequest.objects.all()
#    features_html = '<h1>Список запросов на улучшение</h1><ul>'
#    for feature in features:
#        features_html += f'<li><a href="{feature.id}/">{feature.title}</a> - {feature.status}</li>'
#    features_html += '</ul>'
#    return HttpResponse(features_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

#class BugDetailView(DetailView):
#    model = BugReport
#    pk_url_kwarg = 'bug_id'
#
#    def get(self, request, *args, **kwargs):
#        bug = self.get_object()
#        response_html = f'<h1>{bug.title} - {bug.status}</h1><p>{bug.description}</p><br><p>Приоритет бага - {bug.priority}</p><br><p>{bug.project} , {bug.task}</p>'
#        return HttpResponse(response_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

#class FeatureDetailView(DetailView):
#    model = FeatureRequest
#    pk_url_kwarg = 'feature_id'
#
#    def get(self, request, *args, **kwargs):
#        self.object = self.get_object()
#        feature = self.object
#        response_html = f'<h1>{feature.title} - {feature.status}</h1><p>{feature.description}</p><br><p>Приоритет - {feature.priority}</p><br><p>{feature.project} , {feature.task}</p>'
#        return HttpResponse(response_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'

def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('tasks:project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})

def add_bug(request):

    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)

            bug.project = project
            bug.save()
            return redirect('quality_control:bug_detail.html')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature(request):

    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.project = project
            feature.task = task
            feature.save()
            return redirect('quality_control:feature_detail')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

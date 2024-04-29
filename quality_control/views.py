from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView, DetailView
# Create your views here.

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = f"<h1>Cистема контроля качества</h1><a href='{bug_list_url}'>Посмотреть список всех багов</a><br><a href='{feature_list_url}'>Перейти к запросам на улучшение</a>"
    return HttpResponse(html)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Посмотреть список всех багов</a><br><a href='{feature_list_url}'>Перейти к запросам на улучшение</a>"
        return HttpResponse(html)

#def bug_list(request):
#   return HttpResponse("Список отчетов об ошибках")

#def feature_list(request):
#    return HttpResponse("Список запросов на улучшение")

#def bug_detail(request, bug_id):
#    return HttpResponse(f"Детали бага {bug_id}")

#def feature_id_detail(request, feature_id):
#    return HttpResponse(f"Детали улучшения {feature_id}")

#def bug_list(request):
#    bugs = BugReport.objects.all()
#    bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
#    for bug in bugs:
#        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a> - {bug.status}</li>'
#    bugs_html += '</ul>'
#    return HttpResponse(bugs_html)

def bug_list(request, bug_id):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug_id}/">{bug.title}</a> - {bug.status}</li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a> - {feature.status}</li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
        return HttpResponse(response_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
        return HttpResponse(response_html)


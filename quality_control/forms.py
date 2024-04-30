from django import forms
from django.forms import ModelForm
from .models import BugReport
from .models import FeatureRequest

class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['project','task', 'title', 'description', 'status', 'priority']

class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['project','task', 'title', 'description', 'status', 'priority']
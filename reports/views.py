from django.shortcuts import render

# Create your views here.
from reports.models import Report

def report_index(request):
    reports = Report.objects.all()
    context = {
        'reports': reports
    }
    return render(request, 'report_index.html', context)



def report_detail(request, pk):
    report = Report.objects.get(pk=pk)
    context = {
        'report': report
    }
    return render(request, 'report_detail.html', context)


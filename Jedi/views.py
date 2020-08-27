from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Project, Dashboard
from django.db.models import Avg
from .forms import DashboardRegistrationForm, ProjectRegistrationForm

def homePage(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def loginPage(request):
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form":form})

def logout_request(request):
    # logout(request)
    # messages.info(request, "Logged out successfully!")
    return HttpResponse("Logged out")

def signup(request):
    return HttpResponse("Signup page")

def projects(request):
    projects = Project.objects.all()
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    dashboards = Dashboard.objects.all()
    overdue_tasks_dashboards = dashboards.filter(due='2')
    context = {
        'avg_projects' : avg_projects,
        'projects' : projects,
        'dashboards' : dashboards,
        'overdue_tasks_dashboards' : overdue_tasks_dashboards,
    }
    return render(request, 'templates/projects.html', context)


def newDashboard(request):
    if request.method == 'POST':
        form = DashboardRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_task.html', context)
        else:
            return render(request, 'projects/new_task.html', context)
    else:
        form = DashboardRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_task.html', context)

def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'templates/projects.html', context)
        else:
            return render(request, 'templates/projects.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'templates/projects.html', context)







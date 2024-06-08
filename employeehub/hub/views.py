from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Department, Employee, Attendance, Overtime
from django.http import JsonResponse
from django.db.models import Q, Count, Sum, F
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import EmployeeCreateForm, AttendanceForm, DepartmentForm, OvertimeForm, OvertimeFilterForm
from collections import defaultdict

# Create your views here.
@login_required
def home(request):
    return render(request,'hub/home.html')


class DepartmentListView(ListView):
    """
    View to list all departments.
    """
    model = Department
    template_name = 'hub/dept_view.html'
    context_object_name = 'object_list'

class DepartmentCreateView(CreateView):
    """
    View to create a new department.
    """
    model = Department
    fields = ['Department_Name']
    template_name = 'hub/dept_create.html'
    success_url = reverse_lazy('department_list')

    def get_context_data(self, **kwargs):
        """
        Add title context to the view.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Department'
        return context

class DepartmentUpdateView(UpdateView):
    """
    View to update an existing department.
    """
    model = Department
    fields = ['Department_Name']
    template_name = 'hub/dept_create.html'
    success_url = reverse_lazy('department_list')

    def get_context_data(self, **kwargs):
        """
        Add title context to the view.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Department'
        return context

class DepartmentDeleteView(DeleteView):
    """
    View to delete a department.
    """
    model = Department
    success_url = reverse_lazy('department_list')

    def delete(self, request, *args, **kwargs):
        """
        Handle the deletion of a department.
        """
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'message': 'Department deleted successfully'}, status=200)

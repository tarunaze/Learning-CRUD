from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
from basic_app.models import School,Student
from django.urls import reverse_lazy
# Create your views here.

class CBV(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = School

class SchoolDeleteView(DeleteView):
    context_object_name = 'deleted'
    model = School
    success_url = reverse_lazy('basic_app:list')

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Client, Lawyer, Case
from .forms import ClientForm, LawyerForm, CaseForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

# Client views


class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = "/clients/"


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = "/clients/"


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('cases:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Client'
        return context

# create Lawyer views
class LawyerListView(ListView):
    model = Lawyer
    template_name = 'lawyers/lawyer_list.html'


class LawyerCreateView(CreateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = 'lawyers/lawyer_form.html'
    success_url = "/lawyers/"


class LawyerUpdateView(UpdateView):
    model = Lawyer
    form_class = LawyerForm
    template_name = 'lawyers/lawyer_form.html'
    success_url = "/lawyers/"


class LawyerDeleteView(DeleteView):
    model = Lawyer
    template_name = 'lawyers/lawyer_confirm_delete.html'
    success_url = reverse_lazy('cases:lawyer_list')
    

# Create Case view


class CaseListView(ListView):
    model = Case
    template_name = 'cases/case_list.html'


class CaseCreateView(CreateView):
    model = Case
    form_class = CaseForm
    template_name = 'cases/case_form.html'
    success_url = "/cases/"


class CaseUpdateView(UpdateView):
    model = Case
    form_class = CaseForm
    template_name = 'cases/case_form.html'
    success_url = "/cases/"


class CaseDeleteView(DeleteView):
    model = Case
    template_name = 'cases/case_confirm_delete.html'
    success_url = reverse_lazy('cases:case_list')

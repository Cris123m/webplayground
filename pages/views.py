from django.views.generic.list import ListView
from .models import Page
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PageForm

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(CreateView):
    model = Page
    form_class=PageForm
    success_url=reverse_lazy('pages')

class PageUpdate(UpdateView):
    model = Page
    form_class=PageForm
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id])+"?ok"

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages')
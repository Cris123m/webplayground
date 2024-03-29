from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class SignUp(CreateView):
    form_class=UserCreationForm
    #success_url=reverse_lazy('login')
    template_name='registration/signup.html'
    def get_success_url(self):
        return reverse_lazy('login')+"?ok"
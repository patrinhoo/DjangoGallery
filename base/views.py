from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Image


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('images')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('images')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('images')
        return super(RegisterPage, self).get(*args, **kwargs)


class ImageList(LoginRequiredMixin, ListView):
    model = Image
    context_object_name = 'images'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = context['images'].filter(user=self.request.user)

        category_input = self.request.GET.get('category-area') or ''
        if category_input:
            context['images'] = context['images'].filter(
                category__icontains=category_input)

        context['category_input'] = category_input

        return context


class ImageDetail(LoginRequiredMixin, DetailView):
    model = Image
    context_object_name = 'image'
    template_name = 'base/image.html'


class ImageAdd(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['title', 'category', 'image']
    success_url = reverse_lazy('images')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ImageAdd, self).form_valid(form)


class ImageDelete(LoginRequiredMixin, DeleteView):
    model = Image
    context_object_name = 'image'
    success_url = reverse_lazy('images')

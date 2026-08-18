from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import UserForm
from .models import CustomUser


class ProfileView(DetailView):
    """Класс просмотра профиля пользователя."""

    model = CustomUser
    template_name = 'profile.html'
    slug_url_kwarg = 'username'
    slug_field = 'username'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """Класс редактирования профиля пользователя."""

    model = CustomUser
    template_name = 'user.html'
    form_class = UserForm

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('users:profile',
                       kwargs={
                           'username': self.request.POST.get('username')})


class RegisrationView(CreateView):
    """Класс для регистрации пользователя."""

    template_name = 'registration_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('metro:index')
